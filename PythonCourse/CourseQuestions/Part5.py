

x = float(6) #turning a integer into a float
print(type(x))

#turning a list into a set
y = [5,3,0,1,6,3,3,4,8,6,1,2,0,5,6]
y_set = set(y)
print(y_set)

#turning a set into a list
y_list = list(y_set)
print(y_list)

#turning a dictionary into a list - you lose all the values but keep the keys
qpr_dict = {'Dieng':1,'Kakay':2,'Paal':3,'Dickie':4,'Dunne':5,'Field':6,'Willock':7,'Adomah':37}
qpr_list = list(qpr_dict)
print(qpr_list)

#range function - creating a list
yo = list(range(1,101))
print(yo)

#using a loop with range
for x in range(1,11) :
    print(x,'counting from 1-10')

#easier way to use range instead of using for loop. called a list comprehension
square_numbers = [x * x for x in range(1,101)]
print(square_numbers)

#list comprehension
vowel_players = [d for d in qpr_list if d[0] in 'AEIOU']
print(vowel_players)

#set comprehension - first letters of names as a set
vowel_players_set = {c[0] for c in qpr_list}
print(vowel_players_set)

#dictionary comprehension - giving each squared number in dict for each num
dict_comp = {n:n * n  for n in range(11)}
print(dict_comp)

new_list = [4,6,1,8,5,4,8,9,9]

#sum function - adding up numbers
p = sum(new_list)
print(p)

#smallest number in list - min
p_min = min(new_list)
print(p_min)

#largest number in list - max
p_max = max(new_list)
print(p_max)

#any function checks if items are true or false (empty list = false)
p_any = any(new_list)
print(p_any)

#all function checks if all items in collection are true. Empty list returns true. 0 = false value
p_all = all(new_list)
print(p_all)

list_numbers = list(range(1,31))
print(list_numbers)

def squares_func(list1):
    squares_list = []
    for x in list1 :
            x * x
    return squares_list

print(squares_func(list_numbers))

list_test = [1,5,4,2,2]

#creating a function using list comprehension
def squares_f(some_list):
    return [x * x for x in some_list]
print(squares_f(list_test))

#creating a function inside another function
def function_f(single_value):
    new_value = single_value + 1
    return new_value

def apply(list_of_items, function_f):
    results = []
    for x in list_of_items:
        results.append(function_f(x))
    return results

print(apply(list_test,function_f))

#list comprehension using a function - much easier
results_easier = [function_f(r) for r in list_test]
print(apply(results_easier,function_f))

