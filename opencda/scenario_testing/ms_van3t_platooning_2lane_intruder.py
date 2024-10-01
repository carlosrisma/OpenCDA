# -*- coding: utf-8 -*-
import os

import carla

import opencda.scenario_testing.utils.cosim_api as sim_api
import opencda.scenario_testing.utils.customized_map_api as map_api
from opencda.core.common.cav_world import CavWorld
from opencda.scenario_testing.evaluations.evaluate_manager import \
    EvaluationManager
from opencda.scenario_testing.utils.yaml_utils import add_current_time
from threading import Event
from opencda.scenario_testing.utils.ms_van3t_cosim_api import MsVan3tCoScenarioManager
import time
import datetime


def run_scenario(opt, scenario_params):
    try:
        scenario_params = add_current_time(scenario_params)

        #  Create log directory
        date = datetime.datetime.now()
        if opt.pldm:
            dir_name = date.strftime('logs_times_pldm_ldm/pldm/log_%d_%m_%H_%M_%S')
        else:
            dir_name = date.strftime('logs_times_pldm_ldm/ldm/log_%d_%m_%H_%M_%S')
        home_dir = os.path.expanduser('~')
        full_path = os.path.join(home_dir, dir_name)
        os.mkdir(full_path)

        cav_world = CavWorld(opt.apply_ml, opt.gpu)

        current_path = os.path.dirname(os.path.realpath(__file__))
        xodr_path = os.path.join(
            current_path,
            '../assets/2lane_freeway_simplified/2lane_freeway_simplified.xodr')
        # xodr_path = os.path.join(
        #     current_path,
        #     '../assets/4lane_freeway/4lane_freeway.xodr')


        # create scenario manager
        scenario_manager = sim_api.ScenarioManager(scenario_params,
                                                   opt.apply_ml,
                                                   opt.version,
                                                   xodr_path=xodr_path,
                                                   cav_world=cav_world,
                                                   carla_host=opt.host,
                                                   carla_port=opt.port)

        single_cav_list = \
            scenario_manager.create_vehicle_manager(application=['single'], log_dir=full_path)

        traffic_manager, bg_veh_list = \
            scenario_manager.create_traffic_carla(port=opt.tm_port)

        step_event = Event()
        stop_event = Event()
        ms_van3t_manager = \
            MsVan3tCoScenarioManager(scenario_params,
                                     scenario_manager,
                                     single_cav_list,
                                     traffic_manager,
                                     step_event=step_event,
                                     stop_event=stop_event,
                                     port=opt.grpc_port)

        spectator = scenario_manager.world.get_spectator()
        spectator_vehicle = single_cav_list[5].vehicle
        transform = spectator_vehicle.get_transform()
        spectator.set_transform(carla.Transform(transform.location +
                                                carla.Location(z=120),
                                                carla.Rotation(pitch=-90)))
        scenario_manager.tick()

        while True:

            transform = spectator_vehicle.get_transform()
            spectator.set_transform(carla.Transform(transform.location +
                                                    carla.Location(z=120),
                                                    carla.Rotation(pitch=-90)))
            init_time = time.time_ns()
            for i, single_cav in enumerate(single_cav_list):
                single_cav.update_info_LDM()
                # control = single_cav.run_step()
                # single_cav.vehicle.apply_control(control)

            print('Time to update LDMs for ', len(single_cav_list), ' vehicles: ',
                  (time.time_ns() - init_time) / 1e6, 'ms')


            for actor in scenario_manager.world.get_actors().filter("*vehicle*"):
                location = actor.get_location()
                scenario_manager.world.debug.draw_string(location, str(actor.id), False, carla.Color(200, 200, 0))

            step_event.set()
            ms_van3t_manager.carla_object.tick_event.wait()
            ms_van3t_manager.carla_object.tick_event.clear()

    finally:
        scenario_manager.close()
        for v in single_cav_list:
            v.destroy()
