import numpy as np
class Engine:
    def findDist(self,a,b,a1,b1):
        return np.sqrt(np.sum([np.square(a-a1),np.square(b-b1)]))