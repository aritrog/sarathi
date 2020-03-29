import numpy as np
import matplotlib.pyplot as plt
import BotDecidesPos
#import matplotlib.pyplot as plt
class BotPool:

    recorder=[]
    def __init__(self):
        pass

    def register(self,nbot):
        self.recorder.append((nbot))
        print(nbot.id,"has been registered")

    def getList(self):
        return self.recorder
    def stimulate(self):
        c=0
        for bot in self.recorder:
            # x=np.random.randn(1)*10.0
            # y = np.random.randn(1) * 10.0
            #tx = np.random.randn(1) * 10.0
            #ty = np.random.randn(1) * 10.0
            x=np.array([0.0,10.0])
            y = np.array([0.0, 0.0])
            tx = np.array([9.0, 0.0])
            ty = np.array([5.0, 17.0])
            bot.setDefPos(x[c],y[c])
            print("Ïnitial refference point of ", bot.id," ïs  x: ",x[c], " y: ", y[c])
            bot.setTarget(tx[c],ty[c])
            print("final refference point of ", bot.id, " ïs  x: ", tx[c], " y: ", ty[c])
            bot.setSpeed(0.8)
            c = c + 1
        for bot in self.recorder:
            while bot.checkTarget() :
                bot.updatePos()
        p=1
        coor=["red","blue","green"]
        fig=plt.figure()
        for bot in self.recorder:
            #ax=plt.subplot(2,1,p)
            c=str(p)
            plt.scatter(bot.plotx,bot.ploty,color=coor[p])
            print(bot.id,bot.plotx,bot.ploty)
            p=p+1
            #plt.show()
            #plt.scatter(bot.plotx,bot.ploty)

        
bp=BotPool()
ob1=OneBot("123bot")
ob2=OneBot("213bot")
bp.register(ob1)
bp.register(ob2)
bp.stimulate()
plt.show()
#mpl.show()
