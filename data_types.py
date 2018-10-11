import numpy as np		#import numpy

#integers

i = 10					#integer
print(type(i))			#print out data type

a_i = np.zeros(i,dtype=int)		#declare array
print(type(a_i))				#return ndarray
print(type(a_i[0]))				#return int64

#floats

x = 119.0				#float
print(type(x))			#print data type

y = 1.19e2				#float in sci not
print(type(y))			#print data type

z = np.zeros(i,dtype=float)		#declare array of floats
print(type(z))					#return nd array
print(type(z[0]))				#return float64