#import Numpy
import numpy as np

#def main function
def main():
	i = 0				#integer i
	x = 119.0			#float x
	
	for i in range(120):		#loop from 0 to 119
		if ((i%2)==0):			#if i is even
			x += 3.				#add 3 to x
		else:					#if odd
			x -= 5.				#subtact 5
			
	s = "%3.2e" % x				#make string containing x with
								#sci notation and two dec places
	print(s)					#print s
	
if __name__ == "__main__":		#run main
	main()