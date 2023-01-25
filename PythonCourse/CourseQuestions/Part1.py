#Exercise 1 - person characteristics
import datetime
from typing import List, Tuple, Dict, Set

first_name = 'Dominik'
second_name = 'Szoboszlai'
dob = datetime.date(2000, 10, 25)
height_metres = 1.86
clubs = ['Liefering', 'Red Bull Salzburg', 'Red Bull Leipzig']
intl_caps = 26
intl_goals = 6
games_per_goal = intl_caps / intl_goals
position = 'Attacking Midfielder'
transfer_fee = '£25,000,000'

print(first_name, second_name)
print("Position:", position)
print("DOB:",dob)
print ("Height:", height_metres,"m")
print ("Average Games Per Goal", games_per_goal)
print("Transfer Fee", transfer_fee)

skills = ["finishing", "heading", "passing", "speed", "tackling"]

print("skills =",skills)

favourite_skill = input("What Is Your Favourite Skill?:")

#if list elements not included in another
if favourite_skill not in skills:
    skills.append(favourite_skill)

else :
    print("that skill already exists")

print(favourite_skill)
print(skills)

skill_dict = {'finishing':81,'heading':65,'passing':85,'speed':73,'tackling':45}
skill_input = input("Input Skill Here:")
skill_num = skill_dict[skill_input] if skill_input in skill_dict else None
if skill_num is None:
    print("no such skill")
elif skill_num > 80 : print("SUPER COOL")
elif skill_num >50 : print("COOL")

def higher_than(dict:Dict,number:int) :
    list_values = []
    for key,value in dict.items() :
        if value >= number :
           list_values.append(key)
    return list_values

print(higher_than(skill_dict,80))


#wallet
wallet = {'GBP': 50.00,'HUF':40000.00,'USD': 80.00,'EUR':25.00}
Pounds = wallet.get('GBP')
print("Amount of GBP:", Pounds)

def working_wallet(wallet_dict:Dict, currency:str, amount_spent:float) -> int:
    for wallet_currency,amount in wallet_dict.items() :
        if currency == wallet_currency :
            if amount_spent <= amount :
                wallet_dict[wallet_currency] -= amount_spent
                return amount_spent
            else :
                wallet_dict[wallet_currency]=0
                return amount

print(working_wallet(wallet, 'GBP', 33))

print("Amount of GBP:", wallet['GBP'])

class EmptyWalletError(Exception):
    pass

def working_wallet2(wallet_dict:Dict, currency:str, amount_spent:float) :
    remaining_amount = wallet_dict.get(currency,0)
    if wallet_dict[currency] >= amount_spent:
        wallet_dict[currency] = remaining_amount - amount_spent
        return min([remaining_amount,amount_spent])
    else:
        raise EmptyWalletError('Not enough money in wallet')

try:
    working_wallet2(wallet,'HUF',1000)
except EmptyWalletError:
    print('you outta money fool')

print(working_wallet2(wallet,'HUF',1000.00))
