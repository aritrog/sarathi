import BotDecidesPos
import numpy as np

class Collision_check:
    def __init__(self):
        self.m=0.0
        self.n=0.0



    def load_data(self,bot):
        tgx,tgy=bot.getTarget()
        mpx,mpy=bot.getPos()
        spd=bot.getSpeed()
        return spd,mpx,mpy,tgx,tgy

    def  checkCollision(self,bot1,bot2):
        eg = Engine()
        sp1,x,y,x1,y1=self.load_data(bot1)
        sp2,a,b,a1,b1=self.load_data(bot2)
        p=eg.findDist(x,y,x1,y1)
        q=eg.findDist(a,b,a1,b1)
        #v1=[sp1*(x-x1)/p,sp1*(y-y1)/p]
        #v2 = [sp2 * (a - a1) / q, sp2 * (b - b1) / q]
        #Ax=C, which is the matrix from of the equation on the path of the vehicle
        s=[[x-x1,y-y1],[a-a1,b-b1]]
        t=[y*x1-x*y1,b*a1-a*b1]
        self.m,self.n=eg.eq_StraightLine(s,t)
        p1=eg.findDist(x,y,self.m,self.n)
        q1=eg.findDist(a,b,self.m,self.n)
        eta1=p1/sp1;
        eta2=q1/sp2;
        if np.absolute(eta1-eta2)<1 :
            return True
        else:
            return False

    def getCollisionIndex(self):
        return self.m,self.n

    def setCollisionIndex(self,a,b):
        self.m=a
        self.n=b
