list_of_numbers = [1,2,3,4,3,4,56,7,8,9,0] #listing an ordered sequence of items with diffrent and can be modified(muttable) datatype using []

print(len(list_of_numbers)) #prints length of the list
print(list_of_numbers[1]) #print the second element of the list using index value 
print(list_of_numbers[-1]) #print the first nember from the end
print(list_of_numbers[1:8])#print from second to fourth element
list_of_numbers.sort()#sorts the elemets of a list
print(list_of_numbers)
list_of_numbers.append(26)#add new element at end
print(list_of_numbers)
#list_of_numbers.insert(1:3)
list_of_numbers[4] = 5#change the value of an index spacified
list_of_numbers[5] = 6
print(list_of_numbers)
list_of_numbers.extend([2,3,4,5,54,5,64,6,4,69])
print(list_of_numbers)

tuple_of_numbers = (1,2,3,4,5,6) #tuple is an ordered sequence of items same as listing the diffrence is tuple elements cant be modified(immutable)

set_of_stuff = {1,23,4,5,'words'} #set stores unique values, not limited with one datatype at a time
#set_of_numbers = set(1,2,3,4,5,6) #also set numbers 


number_dictionary = {'name':'jer','age':21,'gender':' helicopter'} #it stores unordered collecton of key and values
print(number_dictionary['name'])
name = 'hana'
print(name[1])#output the second letter