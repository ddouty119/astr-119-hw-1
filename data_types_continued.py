#string

s = "I am a string."
print(type(s))			#will say str

#Booleans

yes = True			#Bool true
print(type(yes))

no = False			#Bool false
print(type(no))

#List - ordered and changeable

alpha_list = ["a", "b", "c"]	#list init
print(type(alpha_list))			#tuple
print(type(alpha_list[0]))		#string
alpha_list.append("d")			#will add "d" to list
print(alpha_list)				#print list

#Tuple - ordered and unchangeable

alpha_tuple = ("a", "b", "c")	#tuple init
print(type(alpha_tuple))		#tuple

try:							#attempt the following
	alpha_tuple[2] = "d"		#this wont work
except TypeError:				#will get type error
	print("We can't add elements to tuples!")	#print this
print(alpha_tuple)		#print tuple