import os ,random,struct,binascii,base64
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
from Crypto import Random
from Crypto.Cipher import AES
import hashlib

class transmit():

	def __init__(self,key):
		self.bs=AES.block_size
		self.key=hashlib.sha256(key.encode()).digest()

	def encrypt(self, raw):
		raw=self. _pad(raw)
		iv= Random.new().read(AES.block_size)
		cipher=AES.new(self.key, AES.MODE_CBC,iv)
		return base64.b64encode(iv + cipher.encrypt(raw))
	
	def decrypt(self, enc):
		enc=base64.b64decode(enc)
		iv= enc[:AES.block_size]
		cipher=AES.new(self.key, AES.MODE_CBC, iv)
		return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')


	def _pad(self, s):
		return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

	@staticmethod
	def _unpad(s):
		return s[:-ord(s[len(s)-1:])]
	

	#this part of the code is not compiled but the rest is while i upload this to github on 14/11/19 1 in the morning	
	def get_data():
		#this peice of code corresponds to a code which is required to form a connection to the arduino
		#that code will be a part of the boot procedure and will hence establish a
		#connection before any funtion of the transmit is called
		#we here crete a object of arduino_connect and use the already completed connection to get data using the arduino

		




ob=transmit("passwordkey")
txt="hi this is a text sample for encrption"
#txt=txt.encode('UTF-8')
print(txt)
while(len(txt)%16!=0):
	txt=txt+"n"

print(ob.encrypt(txt))
print(ob.decrypt(ob.encrypt(txt)))		
