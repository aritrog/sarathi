import tensorflow as tf
from PIL import Image as image
import numpy as np
import matplotlib.pyplot as plt

'''ímporting the data set''' 
Y=[]
names=[]
file=open('TsignRecgTrain4170Annotation.txt','r')
lines=file.readlines()
m=len(lines)
for line in lines:
	nm,l,w,rx1,ry1,rx2,ry2,tp,waste=str(line).split(';')
	names.append(nm)
	Y.append(tp)
	
'''creating the x part ready'''	
td=[]
for name in names:
	img=image.open(name)
	img=img.resize((100,100))
	img=img.convert('L')
	tt=np.array(img)
	tt=tt.flatten()
	td.append(tt)
	
trainx=np.array(td)	
print(trainx.shape)

'''creating the y part ready'''
fy=[]	
for  y in range(m):
	ty=np.zeros(shape=(57))
	ty[int(Y[y])-1]=1
	fy.append(ty)

trainy=np.array(fy)
print(trainy.shape)

'''defining the learning rate'''

lrng_rt=0.01

''' defining the sigmoid and the relu function'''

def sigmoid(z):
	s=1/(1+np.exp(-z))
	return s
	
def ReLU(z):
	r=np.maximum(0,z)
	return r

'''defining the derivative of the above functions'''

def gsigmoid(z):
	s=sigmoid(z)*(1-sigmoid(z))
	return s

'''preparing the parameters'''

''' the idea is to create a multilayer neural neytwork with all this inpouts, this
	is a vectorised inputs where each 'X'has 10000 columns. For the same in the following lines
	we are going to create the parameters W1,W2,b1,b2, which corresponds tp two layes 1 hidden and
	the other is the outpout layer. The hidden lkayer con=sists of 128n units and the out put layer
	will have 57 units as there is 57 specifications'''
print(trainx.shape)
trainx=np.transpose(trainx)
print(trainx.shape)
trainy=np.transpose(trainy)
'''normalising the dataset'''

trainx=trainx/255
trainy=trainy/255

'''assigning the weights/constants'''

W1=np.random.randn(128,trainx.shape[0])*0.01
b1=np.zeros(shape=(128,trainx.shape[1]))
W2=np.random.rand(57,128)*0.01
b2=np.zeros(shape=(57,trainx.shape[1]))

Cost=[]

'''declaring number of iterations'''

epochs=1000

''' forward propagation''' 


''' for layer 1''' 

iter=[]


for i in range(epochs):
	iter.append(i)

	Z1=np.dot(W1,trainx)
	Z1=Z1+b1
	A1=ReLU(Z1)
	
	'''for the second layer'''
	
	Z2=np.dot(W2,A1)
	Z2=Z2+b2
	A2=sigmoid(Z2)
	
	'''calculating the cost'''
	
	m=trainy.shape[1]
	cost= (-1 / m) * np.sum(np.multiply(trainy, np.log(A2)) + np.multiply(1 - trainy, np.log(1 - A2)))
	print(cost)
	Cost.append(cost)
	
	''' the following formulae is derived by differentiating the cost with respect to A2
	    this is a partial differentiation
	    this is the initialising step for backward propagation                           '''
		
	
	dA2 = - (np.divide(trainy, A2) - np.divide(1 - trainy, 1 - A2))
	
	'''Backward propagation begins'''
	
	'''for layer 2'''
	
	dZ2=dA2*gsigmoid(Z2)
	dW2=(1/m)*np.dot(dZ2,np.transpose(A1))
	db2=(1/m)*np.sum(dZ2,axis=1,keepdims=True)
	dA1=np.dot(np.transpose(W2),dZ2)
	
	''' now we perform gradient descent'''
	
	W2=W2-lrng_rt*dW2
	b2=b2-lrng_rt*db2
	
	'''for layer 1 hidden layer'''
	
	dZ1=dA1*gsigmoid(Z1)
	dW1=(1/m)*np.dot(dZ1,np.transpose(trainx))
	db1=(1/m)*np.sum(dZ1,axis=1,keepdims=True)
	
	'''and gradient descent'''
	
	W1=W1-lrng_rt*dW1
	b1=b1-lrng_rt*db1


plt.plot(np.squeeze(Cost))
plt.ylabel('cost')
plt.xlabel('iterations (per hundreds)')
plt.title("Learning rate =" + str(lrng_rt))
plt.show()



