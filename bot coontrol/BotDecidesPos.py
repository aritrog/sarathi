import numpy as np
import time as tm
import matplotlib.pyplot as mpl
class OneBot():


    id=""

    def __init__(self,name):
        self.id=name
        self.mpos=np.zeros(shape=(2))#the current position in m
        self.macc=np.zeros(shape=(2)) #the current acceleration in m/s^2
        self.mvel=np.zeros(shape=(2))
        self.tpos=np.zeros(shape=(2))
        self.sp=0.0
        self.plotx=[]
        self.ploty=[]

    def updatePos(self) :
        x,y=self.getPos()
        tx,ty=self.getTarget()
        mpos=np.array([x,y])
        tpos=np.array([tx,ty])
        mdiff=[(tpos[0] - mpos[0]),( tpos[1]-mpos[1])]
        mod=mdiff[0]*mdiff[0]+mdiff[1]*mdiff[1]
        mod=np.sqrt(mod)
        if mod<2.0 :
            brake=0.4
        else :
            brake=1
        uvec=[ mdiff[0]/mod ,mdiff[1]/mod ]
        mvel=[self.sp*uvec[0]*brake,self.sp*uvec[1]*brake]
        mpos[0]=mvel[0]*1.0+mpos[0]
        mpos[1]=mvel[1]*1.0+mpos[1]
        #print(mdiff,mod,uvec,mvel,mpos,tpos)
        print("current pos of ",self.id," x: " ,mpos[0],"y: ",mpos[1])
        self.setDefPos(mpos[0],mpos[1])
        self.plotx.append(mpos[0])
        self.ploty.append(mpos[1])

    @property
    def getSpeed(self):
        return self.sp

    def setSpeed(self, newsp):
        self.sp=newsp

    def setTarget(self,x,y):
        self.tpos=[x,y]

    def setDefPos(self, x, y):
        self.mpos = [x, y]
        self.plotx.append(self.mpos[0])
        self.ploty.append(self.mpos[1])

    def getPos(self):
        return self.mpos[0],self.mpos[1]

    def getTarget(self):
        return self.tpos[0],self.tpos[1]


    def checkTarget(self):

        if  (self.tpos[0] + self.sp > self.mpos[0] > self.tpos[0] - self.sp) and  (
                self.tpos[1] + self.sp > self.mpos[1] > self.tpos[1] - self.sp) :
            #print("goal seeking")
            #mpl.scatter(self.plotx,ploty)
            return False
        else :
            return True

#"""
ob=OneBot("botA")
ob.setSpeed(0.6)
#s1=5.0
#s2=7.0
map=np.array([[0.0,0.0],[3.0,1.0],[1.0,4.5],[14.0,8.0],[21.0,11.0]])
#map=np.array([[0.0,0.0],[5.0,8.0]])
for i in range(1,map.shape[0]):

    ob.setTarget(map[i][0],map[i][1])
    ob.setDefPos(map[i-1][0],map[i-1][1])
    print("Ïnitial refference point x: ",map[i-1][0]," y: ",map[i-1][1])
    while ob.checkTarget() :

        #s1=s1+1
        #s2=s2-0.8
        #ob.setTarget(s1, s2)
        ob.updatePos()

mpl.scatter(ob.plotx,ob.ploty)
mpl.show()
#"""




