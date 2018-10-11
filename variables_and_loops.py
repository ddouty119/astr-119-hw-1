import numpy as np		#import numpy lib

def main():			
	i = 0				#declare integer
	n = 10				#another integer
	x = 119.0			#this is a float "."
	
	#numpy can be used to declare arrays
		
	y = np.zeros(n,dtype=float)		#10 zeros as floats
	
	#use for loop to iterate with a variable
	
	for i in range(n):		#i in range [0,n01]
		y[i] = 2.0 * float(i) + 1.	#set y = 2i+1 as float
		
	#iterate through a variable
		
	for y_element in y:
		print(y_element)

#execute the function
	
if __name__ == "__main__":
	main()