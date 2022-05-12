
#numbers = [1,2334,34323,4234131,1,1,1,1234,2,4,43,44,32,344,4,3,2,5,6,75,5,6,7,5,3]

#numburs = [1,2334,34323,4234131,1,1,1,1234,2,4,43,44,32,344,4,3,2,5,6,75,5,6,5,5,5,5,5,5,7,5,3]
#counter = 0
#num = numbers[0]	
#for i in numbers:
#	curr_frequency = numbers.count(i)
#	if(curr_frequency> counter):
#		counter = curr_frequency
#		num = i
#print(num)

# Program to find most frequent
# element in a list

List = [1,2334,34323,4234131,1,1,1,1234,2,4,43,44,32,344,4,3,2,5,6,75,5,6,5,5,5,5,5,5,7,5,3]
counter = 0
num = List[0]
	
for i in List:
	curr_frequency = List.count(i)
	if(curr_frequency> counter):
		counter = curr_frequency
		num = i
print(num)

