
#testing lists and editing lists

ages = [25,26,26,31,63,19,56,91,44]
ages_2 = [45,23,98,55,32]

#adding to a list - append only adds 1
ages.append(6)

#deletes indexed object from list - only deletes 1
ages.pop(0)

#removes a certain object in list - only the first one that appears
ages.remove(26)

#deletes more than one indexed objects in list
del ages[1:3]

#changing the value of one of the objects in the list
ages[0] = 25

print(ages)

test_tuple = (2,6,9,3,7,2,7,3,9,9,6,8,1)

test_set = {1,2,3,4,7,9}

unique_elements = set(test_tuple)

print(test_tuple)

print(test_set)

#merging 2 lists
merged_ages_list = ages + ages_2
print(merged_ages_list)

#slicing lists
sliced_ages = ages_2[0:5]
print(sliced_ages)
print(ages_2)

#turning list into set or tuple
new_set = set(sliced_ages)
print(new_set)

#finding out a data type
x = 0.45
print(type(x))

#enum data type, class
from enum import Enum

class teams :
    qpr = 3
    swansea = 4
    blackpool = 5
    sunderland = 6

print(teams.qpr)

print(type(teams))