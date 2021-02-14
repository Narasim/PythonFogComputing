# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:33:58 2021

@author: TOSHIBA
"""
import distance
import applications
import load_data

class Makespan():
    """ This class will calculate the makespan time of a given plan
        Required parameters for object creation:
            - Plan
        functions:
            - calculate_mkspan()
            - other setter and getter functions
            
    """
    def __init__(self, plan):
        self.makespan_time = 0
        self.plan = plan
        self.apps_count = 5
        self.modules_in_app = 5
        self.apps = load_data.create_load_applications(self.apps_count, self.modules_in_app)
        self.app_mkspan = []
        self.distances = load_data.load_distances()
        
    
    def calculate_mkspan(self):
#        print(self.plan)
#        print(self.makespan_time)
#        print(self.apps[1].modules[0].get_mk_span())
#        print(self.distances.get_dist_to_cloud())
#        total_mkspan = 0 # This variable is used to update the overall makespan time(self.makespan_time)
        for i in range(self.apps_count * self.modules_in_app): # Iterate for the entire plan
            if self.plan[i] == 0: # If placed in Cloud
                self.makespan_time = self.makespan_time + self.apps[int(i/5)].modules[i%5].get_mk_span() + (2*self.distances.get_dist_to_cloud())
#                print("i = ", i, "plan val = ", self.plan[i], "makespan_time = ", self.makespan_time, "distance = ", (2*self.distances.get_dist_to_cloud()))
            elif self.plan[i] == 1: # If placed in Fog Orchestration Node(FCN)
                self.makespan_time = self.makespan_time + self.apps[int(i/5)].modules[int(i%5)].get_mk_span()
#                print(i, self.plan[i], self.makespan_time)
            elif self.plan[i] == 2: # If placed in Neighbor Fog Orchestration Node(NFCN)
                self.makespan_time = self.makespan_time + self.apps[int(i/5)].modules[int(i%5)].get_mk_span() + (2*self.distances.get_dist_to_NFCN())
#                print(print(i, self.plan[i], self.makespan_time, (2*self.distances.get_dist_to_NFCN())))
            else : # If placed in Fog Node
                self.makespan_time = self.makespan_time + self.apps[int(i/5)].modules[int(i%5)].get_mk_span() + (self.distances.get_dist_to_fognode())
#                print(i, self.plan[i], self.makespan_time, (2*self.distances.get_dist_to_fognode()))
            if i%5 == 4: # To calcuate each app's makespan time
#                print(self.makespan_time)
                self.app_mkspan.append(self.makespan_time) # After calculating an app's makespan time, append the value to the list(app_mkspan)
                # This list will contain the makespan time of each app
#                total_mkspan = total_mkspan + self.makespan_time # This variable will contain the plan's makespan time, this value will be updated to the main makespan time at the end
#                print(total_mkspan)
#                print(self.makespan_time)
                self.makespan_time = 0 # Reassign to 0, so that we can calculate makespan for other apps
#                print(self.makespan_time)
        self.makespan_time = sum(self.app_mkspan) # Final make span time is updated
#        print(sum(self.app_mkspan))
        return self.app_mkspan # returns each app's makespan time as a list
    
    def get_makespan_time(self):
        return self.makespan_time
    def set_makespan_time(self, mk_time):
        self.makespan_time = mk_time



        