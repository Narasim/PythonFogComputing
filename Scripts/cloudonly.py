# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:56:20 2021

@author: TOSHIBA
"""

import plan
class Cloudonly():
    def __init__(self, devices, apps, apps_count, modules_in_app, each_device_count, plan_size):
        self.devices = devices
        self.apps = apps
        self.apps_count = apps_count
        self.modules_in_app = modules_in_app
        self.each_device_count = each_device_count
        self.plan_size = plan_size
    
    def run_cloudonly(self):
        cloud_plan = plan.Plan(self.plan_size)
        for i in range(self.apps_count):
            for j in range(self.modules_in_app):
                if(self.devices[0].get_device_availability()):
                    if(self.apps[i].modules[j].get_required_mips() <= self.devices[0].get_amips()):
                        cloud_plan.update_plan(0, i*5+j)
                        self.devices[0].set_amips(self.devices[0].get_amips() - self.apps[i].modules[j].get_required_mips())
                        if(self.devices[0].get_amips() <= 0):
                            self.devices[0].set_device_availability(0)
                else:
                    break
        return cloud_plan.get_plan()
    
        
                    
                    
        