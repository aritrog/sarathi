import pandas as pd
from sklearn.preprocessing import LabelEncoder as lbe
from sklearn.preprocessing import OneHotEncoder as ohe
from sklearn.preprocessing import Imputer as imp
from sklearn.preprocessing import StandardScaler as ss
from sklearn.cross_validation import train_test_split as tts


class dataready(object):
	
	
	def __init__(self,location,split=0.2):
		self.location=location
		datas1 = pd.read_csv(location)
		self.x=datas1.iloc[:,:-1].values
		self.y=datas1.iloc[:,-1].values
		self.xtr,self.xte,self.ytr,self.yte=tts(self.x,self.y,test_size=split)
		self.t=0
		self.tt=self.t+1

#computes all the missing data		
	def mval(self):	
		imp1=imp(missing_values="NaN",strategy="mean",axis=0)
		imp1=imp1.fit(self.x[:,1:3])
		return imp1.transform(self.x[:,1:3])

#turns your non-integer non-float data to integer data, use basically
#for categorical data
#here t=the starting coloumn, and tt is the ending coloumn 
#mind you the tt is not the coloumn next to the ending one		
	def lencx(self,t):
		lbex=lbe()
		return lbex.fit_transform(self.x[:,t:tt+1])

#turns your categorical data into multiple coloumns takes the coloumn of
#categorical data as input	
	def catf(self,t):
		ohe1=ohe(categorical_features=[t])
		return ohe1.fit_transform(self.x).toarray()

#turns your non-integer non-float data to integer data, use basically
#for categorical data type for the output 
	def lency(self):	
		lbey=lbe()
		return lbey.fit_transform(self.y)

#this function applies feature scaling to your data		
	def scal(self):
		ss1=ss()
		self.xtr=ss1.fit_transform(self.xtr)
		self.xte=ss1.transform(self.xte)
		return self.xtr,self.xte
		
	def disp(self):
		print(self.xtr)
		print(self.ytr)
		print(self.xte)
		print(self.yte)
		
	def default(self):
		self.xtr,self.ste = self.scal()
		return self.xtr,self.ytr,self.xte,self.yte
	

			
		
		
		
		
		
	
	
#code to be included for feature engineering with later updates
