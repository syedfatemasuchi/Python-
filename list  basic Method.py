#Create a list and print all its elements.
list = [2,5,3,9,7]
print(list)
#Find the length of a list
print(len(list))
#Print the first and last element of a list.
print(list[0])
print(list[-1])
#Print all elements of a list in reverse order.
list.reverse()
print(list)
#Insert Element 
list.insert(1,3)
print(list)
#Remove element
list.remove(3)
print(list)
#pop element
list.pop(3)
print(list)
3
#add ekement in the end 
list.append(8)
print(list)
#sort element  in ascending order 
list.sort()
print(list)
#sort element in descending order
list.sort(reverse=True)
print(list)
#sum  of all numbers in list
total = sum(list)
print("sum : ",total)

#max num in list 
max= max(list)
print("max :",max)

#min num in list 
min= min(list)
print("min :",min)

#clear
list.clear()
print(list)