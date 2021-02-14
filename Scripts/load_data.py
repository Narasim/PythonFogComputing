# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:18:41 2021

@author: Y NARASIMHULU
"""

import numpy as np
import pandas as pd
import device
import applications
import distance


def create_load_devices(each_device_count):
    """This function creates required number of devices and loads data into each device
        each_device_count is the count of each device type in the architecture
    """
    
#    Loading the data from the csv file
    device_data = np.array(pd.read_csv("../Data/topology.csv",header=None))
#    Creating an array of devices
    devices = []
    loc = 0
    id = 0
#    Loading the data into the devices and assigning an ID to each device.
    type_index = 0
    for i in each_device_count:
        for j in range(i):
#            Pointing the Device class to devices attribute, simply making devices array of type Device
            devices.append(device.Device())
#            assigning values
            devices[id].set_amips(int(device_data[loc][0]))
            devices[id].set_aram(int(device_data[loc][1]))
            devices[id].set_astorage(int(device_data[loc][2]))
            devices[id].set_wenergy(int(device_data[loc][3]))
            devices[id].set_speedmips(int(device_data[loc][4]))
            devices[id].set_tau(float(device_data[loc][5]))
            devices[id].set_additional(int(device_data[loc][6]))
#            ID's are assigned sequentially
            devices[id].set_id(int(id))
            devices[id].set_device_type(type_index)
            id = id + 1
        type_index = type_index + 1
        loc = loc + 1
    return devices
    
# Use the Below code to check the devices data

#for id in range(np.sum(each_device_count)):
#    print('amips = ',devices[id].get_amips())
#    print('aram = ',devices[id].get_aram())
#    print('astorage = ',devices[id].get_astorage())
#    print('wenergy = ',devices[id].get_wenergy())
#    print('speedmips = ',devices[id].get_speedmips())
#    print('tau = ',devices[id].get_tau())
#    print('additional = ',devices[id].get_additional())
#    print('id = ',devices[id].get_id())
#    print('device type = ', devices[id].get_device_type())



def create_load_applications(apps_count, modules_in_app):
    apps_data = np.array(pd.read_csv("../Data/Apps.csv",header=None))
    modules_data = np.array(pd.read_csv("../Data/modules.csv",header=None))
    apps = []
    for i in range(apps_count):
        apps.append(applications.Applications(modules_in_app))

    
#    print(apps_data)
#    print(modules_data)
    for i in range(apps_count):
        apps[i].set_a_id(i)
        apps[i].set_deadline(apps_data[i][0])
        apps[i].set_deployment_time(apps_data[i][1])
        for j in range(modules_in_app):
            apps[i].modules[j].set_m_id(i * apps_count + j)
            apps[i].modules[j].set_required_mips(modules_data[j][0])
            apps[i].modules[j].set_required_ram(modules_data[j][1])
            apps[i].modules[j].set_required_storage(modules_data[j][2])
            apps[i].modules[j].set_mk_span(modules_data[j][3])
    return apps

# Use the below code to get the applications and modules data.
#reach the applications.py for more functions in the classes
#for i in range(apps_count):
#    for j in range(modules_in_app):
#    printing the id of the modules
#        print(apps[i].modules[j].get_m_id())


def load_distances():
    distances = np.array(pd.read_csv("../Data/distances.csv",header=None))
    distance_obj = distance.Distance()
#    print(distances[0])
    distance_obj.set_dist_to_fognode(float(distances[0]))
    distance_obj.set_dist_to_FCN(float(distances[1]))
    distance_obj.set_dist_to_NFCN(float(distances[2]))
    distance_obj.set_dist_to_cloud(float(distances[3]))
    
    return distance_obj

# Use the below code to check the distances
#temp_dist = load_distances()
#print(temp_dist.get_dist_to_FCN())








#import fog_device
#import fog_o
#import plan

#Loading Cloud Data
#cloud_data = pd.read_csv("../Data/topology.csv",header=None)
# print(cloud_data[0:1][:])
# Create an instance of the cloud
#cloud_node = Cloud()
# From the first row of the topology data, read the attributes of the cloud and store them in the cloud object
#cloud_node.set_amips(int(cloud_data[0:1][0]))
#cloud_node.set_aram(int(cloud_data[0:1][1]))
#cloud_node.set_astorage(int(cloud_data[0:1][2]))
#cloud_node.set_wenergy(int(cloud_data[0:1][3]))
#cloud_node.set_speedmips(int(cloud_data[0:1][4]))
#cloud_node.set_tau(float(cloud_data[0:1][5]))
#cloud_node.set_additional(int(cloud_data[0:1][6]))
#cloud_node.set_id(int(0))
#print("amips =",cloud_node.get_amips(),"\naram = ", cloud_node.get_aram(), "\nastorage = ",cloud_node.get_astorage(), "\nwenergy = ",cloud_node.get_wenergy(), "\nspeedmips = ",cloud_node.get_speedmips(), "\ntau = ", cloud_node.get_tau(), "\nID = ",cloud_node.get_id(),"\nadditional time = ",cloud_node.get_additional())
#
#print(cloud_node.get_amips())


#Loading Fog Device Data
# Reading the topology data from the csv file    
#fog_device_node_data = pd.read_csv("../Data/topology.csv",header=None)
# print(fog_o_node_data[1:2][:])
# Create an instance of the Fog Orchestration Class
#fog_device_node = []
#fog_devices_count = 10 
#id = 3
#for i in range(0,fog_devices_count):
#    fog_device_node.append(Fog_Device())
## From the second row of the topology data, read the attributes of the cloud and store them in the cloud object
#    fog_device_node[i].set_amips(int(fog_device_node_data[3:4][0]))
#    fog_device_node[i].set_aram(int(fog_device_node_data[3:4][1]))
#    fog_device_node[i].set_astorage(int(fog_device_node_data[3:4][2]))
#    fog_device_node[i].set_wenergy(int(fog_device_node_data[3:4][3]))
#    fog_device_node[i].set_speedmips(int(fog_device_node_data[3:4][4]))
#    fog_device_node[i].set_tau(float(fog_device_node_data[3:4][5]))
#    fog_device_node[i].set_additional(int(fog_device_node_data[3:4][6]))
#    fog_device_node[i].set_id(int(id))
#    id = id + 1
#    print("amips =",fog_device_node[i].get_amips(),"\naram = ", fog_device_node[i].get_aram(), "\nastorage = ",fog_device_node[i].get_astorage(), "\nwenergy = ",fog_device_node[i].get_wenergy(), "\nspeedmips = ",fog_device_node[i].get_speedmips(), "\ntau = ", fog_device_node[i].get_tau(), "\nID = ",fog_device_node[i].get_id(),"\nadditional time = ",fog_device_node[i].get_additional())
    
#Loading Fog Orchesthration Nodes Data

# Reading the topology data from the csv file    
#fog_o_node_data = pd.read_csv("../Data/topology.csv",header=None)
# print(fog_o_node_data[1:2][:])
# Create an instance of the Fog Orchestration Class
#fog_o_node = []
#fog_o_node.append(Fog_O())
# From the second row of the topology data, read the attributes of the cloud and store them in the cloud object
#fog_o_node[0].set_amips(int(fog_o_node_data[1:2][0]))
#fog_o_node[0].set_aram(int(fog_o_node_data[1:2][1]))
#fog_o_node[0].set_astorage(int(fog_o_node_data[1:2][2]))
#fog_o_node[0].set_wenergy(int(fog_o_node_data[1:2][3]))
#fog_o_node[0].set_speedmips(int(fog_o_node_data[1:2][4]))
#fog_o_node[0].set_tau(float(fog_o_node_data[1:2][5]))
#fog_o_node[0].set_additional(int(fog_o_node_data[1:2][6]))
#fog_o_node[0].set_id(int(1))
#print("amips =",fog_o_node[0].get_amips(),"\naram = ", fog_o_node[0].get_aram(), "\nastorage = ",fog_o_node[0].get_astorage(), "\nwenergy = ",fog_o_node[0].get_wenergy(), "\nspeedmips = ",fog_o_node[0].get_speedmips(), "\ntau = ", fog_o_node[0].get_tau(), "\nID = ",fog_o_node[0].get_id(),"\nadditional time = ",fog_o_node[0].get_additional())


# Create an instance of the Fog Orchestration Class
#fog_o_node.append(Fog_O())
# From the second row of the topology data, read the attributes of the cloud and store them in the cloud object
#fog_o_node[1].set_amips(int(fog_o_node_data[2:3][0]))
#fog_o_node[1].set_aram(int(fog_o_node_data[2:3][1]))
#fog_o_node[1].set_astorage(int(fog_o_node_data[2:3][2]))
#fog_o_node[1].set_wenergy(int(fog_o_node_data[2:3][3]))
#fog_o_node[1].set_speedmips(int(fog_o_node_data[2:3][4]))
#fog_o_node[1].set_tau(float(fog_o_node_data[2:3][5]))
#fog_o_node[1].set_additional(int(fog_o_node_data[2:3][6]))
#fog_o_node[1].set_id(int(2))
#print("amips =",fog_o_node[1].get_amips(),"\naram = ", fog_o_node[1].get_aram(), "\nastorage = ",fog_o_node[1].get_astorage(), "\nwenergy = ",fog_o_node[1].get_wenergy(), "\nspeedmips = ",fog_o_node[1].get_speedmips(), "\ntau = ", fog_o_node[1].get_tau(), "\nID = ",fog_o_node[1].get_id(),"\nadditional time = ",fog_o_node[1].get_additional())



#Loading the Plan
#s = Plan()
#print(s.get_plan_size())
#s.add_to_plan(1)
#s.add_to_plan(2)
#print(s.get_plan_size())
#print(s.get_plan())