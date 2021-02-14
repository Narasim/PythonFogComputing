# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:21:45 2021

@author: TOSHIBA
"""

import load_data
import cloudonly
import edgeward
import genetic
import makespan
import fogcloud
import deployment_time
import my_genetic

def run_final_edgeward(apps_count, modules_in_app, each_device_count, plan_size):
    print("*************Edge Ward Placement*************")
    devices = load_data.create_load_devices(each_device_count) # Creating devices and loading the data
    apps = load_data.create_load_applications(apps_count, modules_in_app) # Creating the apps and loading the data
    edge_ward_obj = edgeward.Edgeward(devices, apps, apps_count, modules_in_app, each_device_count, plan_size)
    edge_ward_plan = edge_ward_obj.run_edgeward()
    print(edge_ward_plan)
    edge_ward_mkspan = makespan.Makespan(edge_ward_plan)
    edge_ward_deployment_time = deployment_time.Deployment_time(edge_ward_plan)
    print(edge_ward_mkspan.calculate_mkspan(), edge_ward_mkspan.get_makespan_time())
    print(edge_ward_deployment_time.calculate_deployment_time())
    calculate_utilization(edge_ward_plan, apps_count, modules_in_app)
    

def run_final_cloudonly(apps_count, modules_in_app, each_device_count, plan_size):
    print("*************Cloud Only Placement*************")
    devices = load_data.create_load_devices(each_device_count) # Creating devices and loading the data
    apps = load_data.create_load_applications(apps_count, modules_in_app) # Creating the apps and loading the data
    cloud_only_obj = cloudonly.Cloudonly(devices, apps, apps_count, modules_in_app, each_device_count, plan_size)
    cloud_only_plan = cloud_only_obj.run_cloudonly() # Running the Cloud-Only
    cloud_only_mkspan = makespan.Makespan(cloud_only_plan)
    cloud_only_deployment_time = deployment_time.Deployment_time(cloud_only_plan)
    print(cloud_only_mkspan.calculate_mkspan(), cloud_only_mkspan.get_makespan_time())
    print(cloud_only_deployment_time.calculate_deployment_time())
    calculate_utilization(cloud_only_plan, apps_count, modules_in_app)
    

def run_final_fogcloud(apps_count, modules_in_app, each_device_count, plan_size):
    print("*************Fog Cloud Placement*************")
    devices = load_data.create_load_devices(each_device_count) # Creating devices and loading the data
    apps = load_data.create_load_applications(apps_count, modules_in_app) # Creating the apps and loading the data
    fog_cloud_obj = fogcloud.FogCloud(devices, apps, apps_count, modules_in_app, each_device_count, plan_size)
    fog_cloud_plan = fog_cloud_obj.run_fogcloud()
    fog_cloud_mkspan = makespan.Makespan(fog_cloud_plan)
    fog_cloud_deployment_time = deployment_time.Deployment_time(fog_cloud_plan)
    print(fog_cloud_mkspan.calculate_mkspan(), fog_cloud_mkspan.get_makespan_time())
    print(fog_cloud_deployment_time.calculate_deployment_time())
    calculate_utilization(fog_cloud_plan, apps_count, modules_in_app)
    

def run_final_genetic(devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans):
    print("*************Genetic Placement*************")
    devices = load_data.create_load_devices(each_device_count) # Creating devices and loading the data
    apps = load_data.create_load_applications(apps_count, modules_in_app) # Creating the apps and loading the data    
    genetic_obj = genetic.Genetic(devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans)
    genetic_obj.run_genetic()
    
def run_final_mygenetic(devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans):
    print("*************My Genetic Placement*************")
    devices = load_data.create_load_devices(each_device_count) # Creating devices and loading the data
    apps = load_data.create_load_applications(apps_count, modules_in_app) # Creating the apps and loading the data
    genetic_obj = my_genetic.MyGenetic(devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans)
    genetic_obj.run_mygenetic()


def calculate_utilization(plan, apps_count, modules_in_app):
    cloud = 0
    FCN = 0
    NFCN = 0
    FN = 0
    for i in plan:
        if(i == 0):
            cloud = cloud + 1
        elif i == 1:
            FCN = FCN + 1
        elif i == 2:
            NFCN = NFCN + 1
        else:
            FN = FN + 1
    print("cloud Utiil = ", cloud/(apps_count*modules_in_app))
    print("FCN Util = ", FCN/(apps_count*modules_in_app))
    print("NFCN Util = ", NFCN/(apps_count*modules_in_app))
    print("FN Util = ", FN/(apps_count*modules_in_app))