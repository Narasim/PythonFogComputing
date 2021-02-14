# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:58:20 2021

@author: TOSHIBA
"""

class Distance():
    """ This class defines the distances between FN to all other nodes
    
        - No initial parameters are required to create an object
        - use the load_data.load_distances() to load the real distances
    """
    def __init__(self):
        self.dist_to_fognode = -1
        self.dist_to_FCN = -1
        self.dist_to_NFCN = -1
        self.dist_to_cloud = -1
    
    def get_dist_to_fognode(self):
        return self.dist_to_fognode
    def set_dist_to_fognode(self, dist_to_fognode):
        self.dist_to_fognode = dist_to_fognode
        
    def get_dist_to_FCN(self):
        return self.dist_to_FCN
    def set_dist_to_FCN(self, dist_to_FCN):
        self.dist_to_FCN = dist_to_FCN
        
    def get_dist_to_NFCN(self):
        return self.dist_to_NFCN
    def set_dist_to_NFCN(self, dist_to_NFCN):
        self.dist_to_NFCN = dist_to_NFCN
    
    def get_dist_to_cloud(self):
        return self.dist_to_cloud
    def set_dist_to_cloud(self, dist_to_cloud):
        self.dist_to_cloud = dist_to_cloud