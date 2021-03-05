# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:40:17 2021

@author: Y NARASIMHULU
"""

class Applications():
    """ This class describes the Applications and its modules
        Required Parameters are:
            - no. of modules in app for init
        Functions are:
            All setter and getter functoions
        It also contains Modules class with no initial parameters required
    """
    
    def __init__(self, modules_in_app):
        self.deadline = 0
        self.deployment_time = 0
        self.a_id = 0
        self.modules = []
        for i in range(modules_in_app):
            self.modules.append(self.Module())
        
    def set_deadline(self, deadline):
        self.deadline = deadline
    def get_deadline(self):
        return self.deadline
    
    def set_deployment_time(self, deployment_time):
        self.deployment_time = deployment_time
    def get_deployment_time(self):
        return self.deployment_time
    
    def set_a_id(self, a_id):
        self.a_id = a_id
    def get_a_id(self):
        return self.a_id
    
    def set_modules_in_app(self, modules_in_app):
        self.modules = []
        for i in range(modules_in_app):
            self.modules.append(self.Module())       
    def get_modules_in_app(self):
        return self.modules_in_app
    
    class Module():
        """ Each Application has modules in it.
            This class describes, creates the modules and loads the data into them
        """
        
        def __init__(self):
            self.required_mips = 0
            self.required_ram = 0
            self.required_storage = 0
            self.m_id = 0
            
        def set_required_mips(self, required_mips):
            self.required_mips = required_mips
        def get_required_mips(self):
            return self.required_mips
        
        def set_required_ram(self, required_ram):
            self.required_ram = required_ram
        def get_required_ram(self):
            return self.required_ram
        
        def set_required_storage(self, required_storage):
            self.required_storage = required_storage
        def get_required_storage(self):
            return self.required_storage
        
        def set_m_id(self, m_id):
            self.m_id = m_id
        def get_m_id(self):
            return self.m_id

        
        
            
#app = Applications(5)
#app.modules[0].set_m_id(5)
#print(app.modules[0].get_m_id())
            
            
        