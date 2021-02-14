# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:33:58 2021

@author: TOSHIBA
"""
import distance
import applications
import load_data

class Deployment_time():
    """ This class will calculate the deployment time of a given plan
        Required parameters for object creation:
            - Plan
        functions:
            - calculate_deployment_time()
            - other setter and getter functions
            
    """
    def __init__(self, plan):
        self.deployment_time = 0
        self.plan = plan
        self.apps_count = 5
        self.modules_in_app = 5
        self.each_device_count = [1,1,1,10]
        self.apps = load_data.create_load_applications(self.apps_count, self.modules_in_app)
        self.devices = load_data.create_load_devices(self.each_device_count)
        self.app_deployment_time = []
        self.tau = 0
        
    
    def calculate_deployment_time(self):
        self.set_deployment_time(0)
        for i in range(self.apps_count): # Iterate for the entire plan
            neighbor_placed = 0
            for j in range(self.modules_in_app):
                if(self.plan[(i*self.apps_count) + j] == 2):
                    neighbor_placed = 1
                    break
            if(neighbor_placed == 1):
                self.deployment_time = self.apps[i].get_deployment_time() + self.devices[2].get_tau() + self.devices[2].get_additional()
            else :
                self.deployment_time = self.apps[i].get_deployment_time()
            self.app_deployment_time.append(self.deployment_time)
            self.set_deployment_time(0)
        
        return self.app_deployment_time
    
    def get_app_deployment_time(self):
        return self.app_deployment_time
    def get_deployment_time(self):
        return self.deployment_time
    def set_deployment_time(self, deployment_time):
        self.deployment_time = deployment_time
        
                    


        