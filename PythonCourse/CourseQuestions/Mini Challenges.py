#Given two lists of equal length, xs and ys , create a dictionary which has elements from xs as keys and the corresponding elements of ys as values, in the same order.
#E.g., given xs = ['a', 'b', 'c', 'd'] and ys = [1, 2, 3, 4] , the dictionary should look like this: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

from typing import List, Dict

ys = ['a','b','c','d']
xs = [1,2,3,4]

dict = {}
for y in ys:
    for x in xs:
        dict[y] = x
        xs.remove(x)
        break
print(dict)

#Write a function is_odd(x) which takes an integer x and returns True if x is an odd and False otherwise. Also write is_even(x) which does the opposite.
def is_odd(x):
    return x % 2 != 0

print(is_odd(25))

def is_even(y):
    return y % 2 == 0

print(is_even(26))

#Write a function surface_area(l, w, h) which calculates the surface area of a box (cuboid) given its 3 dimension - length, width and height.

def surface_area(l,w,h):
    lw = l*w
    wh = w*h
    hl = h*l
    sa = lw + wh + hl
    return sa*2

print(surface_area(5,3,4),'cm2')

#given two dictionaries (each of arbitrary length), produce a new dictionary by merging the keys / values of the original two dicts. So if you have e.g. d1 = {'a': 1, 'c': 3, 'e': 6} and d2 = {'b': 2, 'd': 4, 'e': 5}, then the new dict should be {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}   (Notice how the second dictionary overwrites the value of e to a new value).  Order of keys doesn't matter.

d1 = {'a':1,'c':3,'e':5,'g':7,'i':9}
d2 = {'b':2,'d':4,'f':6,'h':8,'j':10}

def merging_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

print(merging_dicts(d1,d2))

#The first function takes a list like this and returns the average score across all students and all subjects.

class_grades = [{'name': 'Maria', 'grades': {'reading': 85, 'writing': 90, 'math': 45}}, {'name': 'Joe', 'grades': {'reading': 68, 'writing': 50, 'math': 40}}, {'name': 'Li', 'grades': {'reading': 90, 'writing': 86, 'math': 92}}]

def avg_score(students:List) -> int:
    total_score = 0
    total_subjects = 0
    for student in students:
        student_grades = student['grades']
        total_score += sum(student_grades.values())
        total_subjects += len(student_grades)
    return total_score / total_subjects

print(avg_score(class_grades))

#The second function takes a list like this, plus the name of a subject (e.g. 'reading'), and returns the average score across all students for that particular subject.

def subject_avg_score(students:List[Dict],subject:str) -> float:
    subject_total_score = 0
    n_of_subjects = 0
    for student in students:
        student_grades = student['grades']
        student_subject = student_grades[subject]
        subject_total_score += student_subject
        n_of_subjects += 1
    return subject_total_score / n_of_subjects

print(subject_avg_score(class_grades,'reading'))

#The third function takes a list like this, plus the name of a subject (e.g. 'reading') and returns a list of student names, sorted with the highest performing students for that subject first. E.g., for 'reading', it should return the list ['Li', 'Maria', 'Joe']

def top_performers_by_subject(students: List[Dict], subject: str) -> List[str]:
    subject_grades = {s['name']: s['grades'][subject] for s in students}
    return sorted(subject_grades, key=subject_grades.get, reverse=True)

print(top_performers_by_subject(class_grades,'reading'))




