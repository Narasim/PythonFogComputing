import numpy as np
class Plan(object):
    """ This class contains the final service placement plan"""
    def __init__(self, size):
        """Initializes the plan"""
        self.size = size
        self.plan = np.full([1,self.size],-1).reshape(self.size) #reshaping the plan to one dimensional
    
#    def __init__(self, size, preplanned):
#        """Initializes the plan"""
#        self.size = size
#        self.plan = np.full([1,self.size],-1).reshape(self.size) #reshaping the plan to one dimensional
#        self.plan = preplanned

    def get_plan_size(self):
        """Returns the plan size"""
        return len(self.plan)
    def set_plan_size(self, size):
        self.size = size
        self.reset_plan()
    
    def update_plan(self, resource_id, loc):
        """Modifies the location of plan to 'resource_id' """
        if( loc > self.size ):
            print("Plan cannot be modified as loc is too high")
        else:
            self.plan[loc] = resource_id
            
    def get_plan(self):
        """Returns the service placement plan"""
        return self.plan
        
    def reset_plan(self):
        """ Resets the plan to empty"""
        self.plan = np.full([1,self.size],-1).reshape(self.size)
    def get_plan_element(self, loc):
        return self.plan[loc]
    


