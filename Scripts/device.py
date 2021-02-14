# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:18:41 2021

@author: Y NARASIMHULU
"""


class Device():
    """ This class describes about the device features and their functionality"""
    
    def __init__(self):
        self.amips = 0 # Available MIPS
        self.aram = 0 # Available RAM
        self.astorage = 0 # Available Storage
        self.wenergy = 0 # Working Energy
        self.speedmips = 0 # Speed of CLoud
        self.tau = 0 # Additinal time if a module runs in cloud
        self.additional = 0 # Additinal time if a module runs in cloud
        self.id = 0
        self.device_type = -1
        self.available = 1 # Device is available if this value is 1 else 0 
        
    def set_amips(self,amips):
        self.amips = amips    
    def get_amips(self):
        return self.amips
        
    def set_aram(self, aram):
        self.aram = aram        
    def get_aram(self):
        return self.aram
    
    def set_astorage(self, astorage):
        self.astorage = astorage        
    def get_astorage(self):
        return self.astorage
    
    def set_wenergy(self, wenergy):
        self.wenergy = wenergy        
    def get_wenergy(self):
        return self.wenergy
        
    def set_speedmips(self, speedmips):
        self.speedmips = speedmips        
    def get_speedmips(self):
        return self.speedmips
        
    def set_tau(self, tau):
        self.tau = tau        
    def get_tau(self):
        return self.tau
        
    def set_additional(self, additional):
        self.additional = additional        
    def get_additional(self):
        return self.additional
        
    def set_id(self, id):
        self.id = id        
    def get_id(self):
        return self.id
    
    def get_device_type(self):
        return self.device_type
    def set_device_type(self, device_type):
        self.device_type = device_type
        
    def get_device_availability(self):
        return self.available
    def set_device_availability(self, status):
        self.available = status
# Reading the topology data from the csv file    
