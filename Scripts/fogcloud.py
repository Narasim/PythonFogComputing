# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:59:01 2021

@author: TOSHIBA
"""


import plan
class FogCloud():
    def __init__(self, devices, apps, apps_count, modules_in_app, each_device_count, plan_size):
        self.devices = devices # Devices data
        self.apps = apps # Apps data
        self.apps_count = apps_count # No. of apps
        self.modules_in_app = modules_in_app # No. of modules in each app
        self.each_device_count = each_device_count # No. of devices of each type
        self.plan_size = plan_size # Plan size
    
    def run_fogcloud(self):
        """This module will place applications only on Fog Devices and """
        fogcloud_plan = plan.Plan(self.plan_size) # Creating an object for plan, initializes all the entries to -1
        app_unsorted = {}
        for i in range(self.apps_count):
#            Findind the paramater for app priority
            app_unsorted[i] = self.apps[i].get_deadline() - self.apps[i].get_deployment_time()
        app_sorted = dict(sorted(app_unsorted.items(), key=lambda item: item[1])) # Sorting the apps based on the parameter obtained above
#        print(app_sorted) # Sorted apps
#        print(app_sorted.keys()) # Sorted apps keys
        
#        We run the through all the app's sensing and actuation modules 
#        We do this because we want to place the sensing and actuation modules in the lowe fog nodes
        for i in app_sorted.keys(): # Iterating according to the priority
            for j in range(self.modules_in_app):
                module_no = self.apps[i].modules[j].get_m_id()%(self.apps_count) # Find the module ID
                if(module_no == 0 or module_no == 4): # Check whether it is sensing or actuation
                    for k in range(3,13): # Place the modules in the lower fog nodes, which range from 3 to 12
#                        print(k, self.devices[k].get_amips(), self.apps[i].modules[j].get_required_mips(),self.devices[k].get_device_availability(),i*5+j,self.plan_size)                        
#                        if(self.devices[k].get_device_availability() == 1):
                        if(self.devices[k].get_amips() >= self.apps[i].modules[j].get_required_mips()): # If available MIPS >= modules required MIPS
                            self.devices[k].set_amips(self.devices[k].get_amips() - self.apps[i].modules[j].get_required_mips()) # Modufy the available MIPS of the device to latest
                            fogcloud_plan.update_plan(k, (i*5)+j) # Update the plan with the current placement
#                            print(k, (i*5)+j)
                            break # Go to nect module in the app
#                                if(self.devices[k].get_amips() <= 0):
#                                    self.devices[k].set_device_availability(0)
        for i in app_sorted.keys():
            for j in range(self.modules_in_app):
                placed = 0
                module_no = self.apps[i].modules[j].get_m_id()%(self.apps_count)
                if(module_no != 0 and module_no != 4): # If the module is not a sense or actuation module
                    iter = 0
                    while(iter < 2 and placed == 0): # Try to place the current module in two iterations, if not placed in the first iteration we place it in the second iteration
                        for k in range(3,13): # Trying to place in the lower fog nodes
    #                        print(k, self.devices[k].get_amips(), self.apps[i].modules[j].get_required_mips(),self.devices[k].get_device_availability(),i*5+j,self.plan_size)                        
    #                        if(self.devices[k].get_device_availability() == 1):
                            if(self.devices[k].get_amips() >= self.apps[i].modules[j].get_required_mips()):
                                self.devices[k].set_amips(self.devices[k].get_amips() - self.apps[i].modules[j].get_required_mips())
                                fogcloud_plan.update_plan(k, (i*5)+j)
#                                print(k, (i*5)+j)
                                placed = 1
                                break
                        if(placed == 0): # If not placed in the lower fog node then place it in the cloud
                            k = 0 # Set device to Cloud
    #                        print(k, self.devices[k].get_amips(), self.apps[i].modules[j].get_required_mips(),self.devices[k].get_device_availability(),i*5+j,self.plan_size)
                            if(self.devices[k].get_amips() >= self.apps[i].modules[j].get_required_mips()):
                                self.devices[k].set_amips(self.devices[k].get_amips() - self.apps[i].modules[j].get_required_mips())
                                fogcloud_plan.update_plan(k, (i*5)+j)
#                                print(k, (i*5)+j)
                                placed = 1 # If placed then try not to place it again, hence this variable is used
                                break
                        iter = iter - 1 # Second iteration
                            
                        
                                
        return fogcloud_plan.get_plan()
                                    
                    
        
        
        
#        Below code is for sorting all modules
#        for i in range(self.apps_count):
#            for j in range(self.modules_in_app):
#                app_unsorted[self.apps[i].modules[j].get_m_id()] = self.apps[i].modules[j].get_required_mips()
##                print(self.apps[i].modules[j].get_m_id(),self.apps[i].modules[j].get_required_mips())
#        print(app_unsorted)
#        app_sorted = dict(sorted(app_unsorted.items(), key=lambda item: item[1]))
#        print(app_sorted)
        
#        return fogcloud_plan.get_plan()