#exceptions - to prevent code breaking when certain things happen e.g. dividing by 0
#use try and except construct in these situations

def bill_split(total_amount:float,n:float) -> float:
    try:
        amount_to_pay = total_amount / n
    except ZeroDivisionError:
        return 0
    return amount_to_pay
#you can use 2 returns in the same function when they have different logical branches
print(bill_split(66.78,4))

#stack data structure, last in first out. using .append & .pop

stack_1 = []
stack_1.append(7)
stack_1.append(4)
stack_1.append(5)
print(stack_1)

#creating custom exceptions
class CustomError(Exception):
    pass

number = 5

def guess_number(num:int) -> str:
    if num > 5:
        return 'good'
    else:
        raise CustomError('Number Too Small')

print(guess_number(6))

try:
    guess_number(4)
except CustomError:
    print('This number is below 5')





