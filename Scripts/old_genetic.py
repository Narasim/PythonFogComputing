# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:08:07 2021

@author: TOSHIBA
"""
import random
import plan
import load_data
import makespan
import deployment_time
import numpy as np
import run_method

class Genetic():
    """This class will run the genetic algorithm"""
    
    def __init__(self, devices, apps, apps_count, modules_in_app, each_device_count, plan_size, no_of_genetic_plans):
        self.devices = devices # Devices data
        self.apps = apps # Apps data
        self.apps_count = apps_count # No. of apps
        self.modules_in_app = modules_in_app # No. of modules in each app
        self.each_device_count = each_device_count # No. of devices of each type
        self.plan_size = plan_size # Plan size
        self.no_of_genetic_plans = no_of_genetic_plans
        self.init_gen_plans = []
        for i in range(self.no_of_genetic_plans):
            self.init_gen_plans.append(plan.Plan(self.plan_size))
        self.nextgen_plans = []
        
    def run_genetic(self):
        no_of_nextgen_plans = 0 # No. of plans that qualified the state check
        for i in range(self.no_of_genetic_plans):#self.no_of_genetic_plans): Generate random plans
            for j in range(self.plan_size):               
                if(j%5 == 0 or j%5 == 4): # Check whether the module is sense or actuation
                    device = random.randint(3,12) # Place sense and actuation in Fog Nodes
                else:
                    device = random.randint(0,2) # Place the process modules in FCN, NFCN or Cloud
#                print(device)
#                 random_palns[] is the plans generated randomly
                self.init_gen_plans[i].update_plan(device, j) # preparing the plans
#            print(self.init_gen_plans[i].get_plan())
            new_devices = load_data.create_load_devices(self.each_device_count) # Create a new object for devices
            # If not created, the old object will be used
            if(self.check_state(self.init_gen_plans[i].get_plan(), new_devices, self.apps)): # Check the state of the randomly generated plan
                self.nextgen_plans.append(plan.Plan(self.plan_size)) # If qualified state check then add the plan to selected list of plans(selected_plans)
                self.nextgen_plans[no_of_nextgen_plans] = self.init_gen_plans[i]
#                print(self.nextgen_plans[no_of_nextgen_plans].get_plan())
                no_of_nextgen_plans = no_of_nextgen_plans + 1 # Counting the no. of plans qualified state check

#        print(no_of_nextgen_plans)
        # Prints all the next generation plans
#        for i in range(no_of_nextgen_plans):
#            print(self.nextgen_plans[i].get_plan())
        # Calculating makespan time of each application in each plan
        genetic_mkspan = [] 
        genetic_dptime = []
        genetic_resptime = []
        for i in range(no_of_nextgen_plans):
#            print(self.nextgen_plans[i].get_plan())
            genetic_mkspan_obj = makespan.Makespan(self.nextgen_plans[i].get_plan()) # calculating the makespan of each plan in next generation plans
            genetic_mkspan.append(genetic_mkspan_obj.calculate_mkspan())
            deployment_time_obj = deployment_time.Deployment_time(self.nextgen_plans[i].get_plan())
            genetic_dptime.append(deployment_time_obj.calculate_deployment_time())
            genetic_resptime.append(np.add(genetic_mkspan[i], genetic_dptime[i]))
#            genetic_resptime.append(genetic_mkspan[i]+genetic_dptime[i])
#        for i in range(no_of_nextgen_plans):
#            print(genetic_mkspan[i], genetic_dptime[i], genetic_resptime[i])
            
#        Calculating the fitness of each next gen plans
        next_gen_plans_fitness = []
        for i in range(no_of_nextgen_plans):
            next_gen_plans_fitness.append(self.calculate_fitness(genetic_resptime[i]))
#        print(next_gen_plans_fitness)
        j = 0
        while(j < 100):
#        fitness of the nextgen plan's sorted indices are rturned
            sorted_indices = np.argsort(next_gen_plans_fitness)
#            for i in sorted_indices:
#                print(next_gen_plans_fitness[i])
#            print("*************")
            non_mutated_plan = self.cross_over(self.nextgen_plans[sorted_indices[0]], self.nextgen_plans[sorted_indices[1]])
            mutated_plan = self.mutate(non_mutated_plan)
            new_devices = load_data.create_load_devices(self.each_device_count)
            if(self.check_state(mutated_plan.get_plan(), new_devices, self.apps )):
                genetic_mkspan[sorted_indices[-1]] = makespan.Makespan(mutated_plan.get_plan()).calculate_mkspan()
                genetic_dptime[sorted_indices[-1]] = deployment_time.Deployment_time(mutated_plan.get_plan()).calculate_deployment_time()
                genetic_resptime[sorted_indices[-1]] = np.add(genetic_mkspan[sorted_indices[-1]], genetic_dptime[sorted_indices[-1]])
                next_gen_plans_fitness[sorted_indices[-1]] = self.calculate_fitness(genetic_resptime[sorted_indices[-1]])
                self.nextgen_plans[sorted_indices[-1]] = mutated_plan
#            print(mutated_plan.get_plan(), genetic_resptime[sorted_indices[-1]], next_gen_plans_fitness[sorted_indices[-1]])
            sorted_indices = np.argsort(next_gen_plans_fitness)
#            for i in sorted_indices:
#                print(next_gen_plans_fitness[i])
            j = j + 1
        print("Plan = ", self.nextgen_plans[sorted_indices[0]].get_plan())
        print("App-wise Makespan Time: ",genetic_mkspan[sorted_indices[0]])
        print("Overall Makespan Time: ", np.sum(genetic_mkspan[sorted_indices[0]]))
        print("Deployment Time: ",genetic_dptime[sorted_indices[0]])
        print("Response Time = ", genetic_resptime[sorted_indices[0]])
        print("Fitness = ", next_gen_plans_fitness[sorted_indices[0]])
        print("Deadline - Response Time = ")
        for i in range(self.apps_count):
            print(self.apps[i].get_deadline() - genetic_resptime[sorted_indices[0]][i])
        run_method.calculate_utilization(self.nextgen_plans[sorted_indices[0]].get_plan(), self.apps_count, self.modules_in_app)
        run_method.energy_consumption(self.nextgen_plans[sorted_indices[0]].get_plan(), self.apps_count, self.modules_in_app, self.each_device_count,1)
            
        
    
    def check_state(self, random_plan_i, devices, apps):
        self.random_plan_i = random_plan_i
        self.new_devices = devices
        self.apps = apps
#        print(self.devices[1].get_amips())
#        print(self.random_plan_i)
        j = 0
        for i in self.random_plan_i: # foe each element in the random plan recieved
#            print(i,j)
#            print(self.new_devices[i].get_amips() , self.apps[int(j/5)].modules[int(j%5)].get_required_mips())
            if(self.new_devices[i].get_amips() < self.apps[int(j/5)].modules[int(j%5)].get_required_mips()):
#            If the required MIPS greater than the avalable MIPS then the check fails(0)
                return 0
            else:
#            If the check qualified then deduct the required MIPS from the available MIPS for the device
                self.new_devices[i].set_amips(self.new_devices[i].get_amips() - self.apps[int(j/5)].modules[int(j%5)].get_required_mips())
            j = j + 1 # To identify the app number and module number
        return 1
    
    def cross_over(self, plan_1, plan_2):
        new_plan = plan.Plan(self.plan_size) # cross over plan is stored in this variable
#        print("Plan1: ",plan_1.get_plan())
#        print("Plan2: ",plan_2.get_plan())
#        We take i locations data from plan1 and i+1 to last locations data from plan2, and perform a cross over to get new_plan
        for i in range(self.plan_size):
            for k in range(0,i+1): # Copy from 0 to i locations data to newplan from plan1
                new_plan.update_plan(plan_1.get_plan_element(k), k)
            for j in range(i+1, self.plan_size): # Copy i+1 to last locations data from plan2 to new_plan
                new_plan.update_plan(plan_2.get_plan_element(j),j)
            new_devices = load_data.create_load_devices(self.each_device_count)
            if(self.check_state(new_plan.get_plan(), new_devices, self.apps)): # Check the state of the new_plan
                return new_plan # If state is satisfied return the new_plan

    def mutate(self, plan_1):
        new_plan = plan.Plan(self.plan_size)
#        print("Non-Mutated plan", plan_1.get_plan())
        # Stuff one random location with a randomly generated device number
        while(True):
            stuff_loc = random.randint(0,self.plan_size-1) # location to stuff
            if((stuff_loc % self.apps_count) == 0 or (stuff_loc % self.apps_count) == 4):
                stuff_val = random.randint(3,12) # Device number to stuff
            else:
                stuff_val = random.randint(0,2) # Device number to stuff
            
            for i in range(self.plan_size):
                if(i == stuff_loc):
                    new_plan.update_plan(stuff_val, stuff_loc) # Stuffing
                else:
                    new_plan.update_plan(plan_1.get_plan_element(i), i) # Keeping other data common
            new_devices = load_data.create_load_devices(self.each_device_count)
            if(self.check_state(new_plan.get_plan(), new_devices, self.apps)):
#                print("Mutated Plan: ", new_plan.get_plan())
                return new_plan
    
    def calculate_fitness(self, response_time):
        fitness_value = 0
        for j in range(self.apps_count):
            if(response_time[j] > self.apps[j].get_deadline()):
                fitness_value = fitness_value + response_time[j] + 1000
            else:
                fitness_value = fitness_value + response_time[j]
        return fitness_value
                   