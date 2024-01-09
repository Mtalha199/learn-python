# LIST
# Lists are used to store multiple items in a single variable
# List items are ordered, changeable, and allow duplicate values.

list=['python','machine-learning','AI']

# Ordered
# It have a defined order, and that order will not change.

list2=['talha','dawood','muavia']
print(list2[0]) # talha

# Changeable
# we can change, add, and remove items in a list after it has been created

#change
list2[0]='Muhammad Talha'
print(list2) #['Muhammad Talha','dawood','muavia']
list2[0:2]=['sani','arslan']
print(list2)

#Add
#Added in diffrent way append() ,insert() ,extend()

#append(if add on the last of the list)

list3=['dsa','oop','db']
list3.append('vs')
print(list3) #['dsa','oop','db','vs']

#insert()
# if add on specific index

list3.insert(0,'vss')
print(list3) # ['vss','dsa','oop','db','vs']

#extend()
list2.extend(list3)
print(list2)

#Remove
#remove by diffrent way (remove(),pop(),clear(),del())

list2.remove('sani')

#pop(it delete the specific data)

list2.pop(1) #it remove the index1 data
list2.pop() #it remove the last of data

# clear()
# it clear the all data but list are remaing

list2.clear()

# del()
# it del the list

del list2

# Allow duplicate
# same name acceptable in list

mylist=['apple','banana','apple','banana']

# List also contain int,string,float

list1=['python',12,True]
print(len(list1))
print(type(list1)) # <class 'list'>

#---------------------------------------------

# TUPLE
# A tuple is a collection which is ordered and unchangeable and allow duplicate value.

tuple=('pakistan','england','india')
print(type(tuple)) # <class 'tuple'>
 

# Ordered
# we can access by index

print(tuple[0]) # pakistan

# dublicate value

tuple=('pakistan','pakistan')
print(tuple)
