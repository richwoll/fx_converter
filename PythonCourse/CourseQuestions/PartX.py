from functools import reduce

list_of_numbers = [4,6,1,9,5,8,2,-1,9,5,3,-5,-6]

#you can edit the first 'n' to both square the numbers and get rid of negatives
positive_numbers = [n for n in list_of_numbers if n >= 0]
print(positive_numbers)

data = [
{'name': 'John', 'gender': 'male', 'spending': 900,'months':['January','April','December']},
    {'name':'Richie','gender':'male','months':['April','December']},
    {'name': 'Alice', 'gender': 'female', 'spending': 1200,'months':[]},
    {'name': 'Bob', 'gender': 'male', 'spending': 500,'months':['December']},
    {'name': 'Eve', 'gender': 'female', 'spending': 1800,'months':['May','November']},
]
#using .get function to get value of dictionary as 'spending' doesn't always appear in data. 0 is to assume 0 when doesn't appear.
total_spending = reduce(
lambda total, record: total + record.get('spending',0),data, 0)
print(total_spending)

#returning average per different dict key
def average_per_gender(data:list) ->dict:
    averages = {}
    spending = {'male':0,'female':0}
    counts = {'male':0,'female':0}
    for record in data:
        gender = record['gender']
        counts[gender] += 1
        spending[gender] += record.get('spending',0)
    averages['male'] = spending['male'] / counts['male']
    averages['female'] = spending['female'] / counts['female']
    return averages
print(average_per_gender(data))

#same but using comprehension
def averages_per_gender2(data:list) -> dict:
    male_data = [m for m in data if m['gender']=='male']
    female_data = [m for m in data if m['gender'] == 'female']
    averages = {
        'male': sum([m.get('spending',0) for m in male_data]) / len(male_data),
        'female': sum([m.get('spending',0) for m in female_data]) / len(female_data)
    }
    return averages
print(averages_per_gender2(data))

product_of_list = reduce(lambda num,num2:num * num2,positive_numbers,1)
print('Product of Numbers in a list:',product_of_list)

even_numbers = [n for n in positive_numbers if (n %2) == 0]
print(even_numbers)

product_of_even_numbers = reduce(lambda even1,even2: even1*even2,even_numbers,1)
print(product_of_even_numbers)

#counting list elements in a dictionary with keys and sorting based on occurance per month
def spending_months(data:list) -> dict:
    dict_spending_months = {'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'September':0,'October':0,'November':0,'December':0}
    for profile in data:
        for month in profile.get('months',[]): #using empty list as default value as not values (number)
            dict_spending_months[month] += 1
    return sorted(dict_spending_months, key=dict_spending_months.get, reverse=True)

print(spending_months(data))

#using Counter function and most common and converting list of lists to a single list
from collections import Counter

def counting_months(data:list) -> dict:
    list_of_months = [n['months'] for n in data]
    list_of_months1 = sum(list_of_months,[])
    counter = Counter(list_of_months1)
    return counter.most_common(12)

print(counting_months(data))