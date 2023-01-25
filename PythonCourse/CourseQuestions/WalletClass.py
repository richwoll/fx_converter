import csv

class Wallet:
    def __init__(self,name:str):
        self.balance = {}
        self.name = name
    def deposit(self,amount:int,currency:str):
        existing_amount = self.balance.get(currency,0)
        self.balance[currency] = existing_amount + amount
    def spend(self,amount:int,currency:str):
        if self.balance.get(currency,0) < amount:
            raise ValueError('Not Enough Money')
        self.balance[currency] -= amount
        return amount
    def show_balance(self,currency:str):
        return self.balance.get(currency,0)
    def export_to_csv(self,filename:str):
        header = ['currency','balance']
        with open('pythonwallettest.csv', 'w') as open_csv:
            writer = csv.writer(open_csv)
            writer.writerow(header)
            for item in self.balance.items():  # `item` here is a tuple
                writer.writerow(item)  # so we can just write it as a row
    def load_from_csv(self,filename:str):
        with open('pythonwallettest.csv', 'r') as read_csv:
            reader = csv.reader(read_csv)
            header = next(reader)
            rows = []
            for row in reader:
                rows.append(row)
                self.balance = dict(rows)





my_wallet = Wallet('my wallet')
my_wallet.deposit(100,'GBP')
my_wallet.deposit(20,'EUR')  # Just so we have more than 1 currency
my_wallet.spend(45,'GBP')
print(my_wallet.show_balance('GBP'))

class Character:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
        self.wallet = Wallet(name + "'s Wallet")
    def give_money(self,other:"Character",amount:int,currency:str):
        self.wallet.spend(amount,currency)
        other.wallet.deposit(amount, currency)

dominik = Character('Dominik',26)
dominik.wallet.deposit(100,'GBP')

jonny = Character('Jonny',29)

dominik.give_money(jonny,20,'GBP')
print(dominik.wallet.show_balance('GBP'))
print(jonny.wallet.show_balance('GBP'))

print(type(dominik))
print(type(dominik.wallet))
print(dominik.wallet.name)

#class inheritence - when you create a new class that inherits the properties and methods of a different 'parent' class

class Character_child(Character):
    pass

print(my_wallet.export_to_csv('pythonwallettest.csv'))
print(my_wallet.load_from_csv('pythonwallettest.csv'))
print(my_wallet.balance)
