# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:18:41 2021

@author: Y NARASIMHULU
"""


import load_data
import run_method



apps_count = 5 #no. of. apps to be considered.
modules_in_app = 5 #no. of. modules in each app.
each_device_count = [1,1,1,10] # each device count
no_of_genetic_plans = 500000
plan_size = apps_count * modules_in_app # Initialize Plan Size
max_iterations = 100
unchanged_iter = 5
devices = load_data.create_load_devices(each_device_count) # Creating devices and loading the data
apps = load_data.create_load_applications(apps_count, modules_in_app) # Creating the apps and loading the data
distances = load_data.load_distances()

print("0\t-Cloud Node\n1\t-Fog Orchestration Node\n2\t-Neighbour Fog Orchestration Node\n3 to 12-Fog Node")
#run_method.run_final_cloudonly(apps_count, modules_in_app, each_device_count, plan_size)

#run_method.run_final_fogcloud(apps_count, modules_in_app, each_device_count, plan_size)

#run_method.run_final_edgeward(apps_count, modules_in_app, each_device_count, plan_size)

#run_method.run_final_genetic(devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans)

run_method.run_final_mygenetic(devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans)

#run_method.run_final_sa(devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans)


#run_method.run_final_hh(max_iterations, unchanged_iter, devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans)


#genetic_obj = my_genetic.MyGenetic(devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans)
#genetic_obj.run_mygenetic()




    