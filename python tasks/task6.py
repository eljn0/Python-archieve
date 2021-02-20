# list with EVEN and ODD number
list = [1,34,56,100,-12,87,987,1,56,67]

# print original list
print ("Original list:")
print (list)

# loop to traverse each element in the list
# and, remove elements
# which are ODD (not divisible by 2)
for i  in list:
	if(i%2 != 0):
	    list.remove(i)

# print list after removing ODD elements
print ("list after removing ODD numbers:")
print (list)


