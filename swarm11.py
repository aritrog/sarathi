"""  """


import math
import subprocess
import numpy as np

def ObstacleForce(p1, p2, rSafe):
    '''Determine the gravitational force between two
    points. Returns a vector'''
    d = math.sqrt(float(math.pow((p1[0] - p2[0]),2) + math.pow((p1[1] - p2[1]),2))) # distance
    if d <= rSafe: # if the obstacle is closer than rSafe, make sure dSqr is a valid value
        dSqr = 0.000001 # if inside safety radius, dSqr should be very very small
    else:
        dSqr = math.pow((d - rSafe),2) # Gravity force is maximum when d = rSafe

    F = G_OBS/dSqr # Repulsive force proportional to 1/dSqr
    unit_vec = [(p1[0] - p2[0])/d, (p1[1] - p2[1])/d]
    f_vec = (unit_vec[0] * F, unit_vec[1] * F) 
    return f_vec, unit_vec,d


class MyBot():
	"""docstring for MyBot"""
	

	def __init__(self,obs,swm,mp,rsafe):
		super(MyBot, self).__init__()
		self.arg = arg
		self.obstacles=obs
		self.swarms=swm
		self.mypos=mp 
		self.sfradius=rsafe



	def collision_detect(self):
		for obj in self.obstacles:
			a,b,c=ObstacleForce(self.mypos,obg,sekf.sfradius)
			