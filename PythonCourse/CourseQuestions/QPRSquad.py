
qpr_kit_numbers = {'Seny Dieng':1,'Osman Kakay':2,'Jimmy Dunne':3,'Rob Dickie':4,'Jake Clarke-Salter':5,'Stefan Johansen':6,'Chris Willock':7,'Luke Amos':8,'Lyndon Dykes':9,'Ilias Chair':10,'Tyler Roberts':11,'Jordan Archer':13,'George Thomas':14,'Sam Field':15,'Niko Hamalainen':16,'Andre Dozell':17,'Macauley Bonne':18,'Taylor Richards':19,'Kenneth Paal':22,'Conor Masterson':23,'Olamide Shodipo':25,'Leon Balogun':26,'Ethan Laird':27,'Sinclair Armstrong':30,'Joe Walsh':32,'Albert Adomah':37,'Tim Iroegbunam':47}

def kit_number(numbers_data:dict,player_name:str) -> int:
    try:
        player_number = numbers_data[player_name]
        return player_number
    except KeyError:
        return 'Wrong Player Name'

print('Kit Number Function:',kit_number(qpr_kit_numbers,'Albert Adomah'))

qpr_squad = [{'name':'Seny Dieng','details':{'number':1,'age':27,'position':'Goalkeeper','height':1.93}},
             {'name':'Osman Kakay','details':{'number':2,'age':25,'position':'Defender','height':1.80}},
             {'name':'Jimmy Dunne','details':{'number':3,'age':25,'position':'Defender','height':1.83}},
             {'name':'Rob Dickie','details':{'number':4,'age':26,'position':'Defender','height':1.93}},
             {'name':'Jake Clarke-Salter','details':{'number':5,'age':25,'position':'Defender','height':1.88}},
             {'name':'Stefan Johansen','details':{'number':6,'age':31,'position':'Midfielder','height':1.82}},
             {'name':'Chris Willock','details':{'number':7,'age':24,'position':'Midfielder','height':1.78}},
             {'name':'Luke Amos','details':{'number':8,'age':25,'position':'Midfielder','height':1.79}},
             {'name':'Ilias Chair','details':{'number':10,'age':25,'position':'Midfielder','height':1.58}},
             {'name':'Tyler Roberts','details':{'number':11,'age':23,'position':'Midfielder','height':1.80}},
             {'name':'Jordan Archer','details':{'number':13,'age':29,'position':'Goalkeeper','height':1.91}},
             {'name':'George Thomas','details':{'number':14,'age':25,'position':'Midfielder','height':1.73}},
             {'name':'Sam Field','details':{'number':15,'age':24,'position':'Midfielder','height':1.91}},
             {'name':'Niko Hamalainen','details':{'number':16,'age':25,'position':'Defender','height':1.84}},
             {'name':'Andre Dozzell','details':{'number':17,'age':23,'position':'Midfielder','height':1.78}},
             {'name':'Macauley Bonne','details':{'number':18,'age':27,'position':'Striker','height':1.80}},
             {'name':'Taylor Richards','details':{'number':20,'age':21,'position':'Midfielder','height':1.80}},
             {'name':'Kenneth Paal','details':{'number':22,'age':21,'position':'Defender','height':1.74}},
             {'name':'Conor Masterson','details':{'number':23,'age':21,'position':'Defender','height':1.91}},
             {'name':'Olamide Shodipo','details':{'number':25,'age':25,'position':'Midfielder','height':1.76}},
             {'name':'Leon Balogun','details':{'number':26,'age':34,'position':'Defender','height':1.90}},
             {'name':'Ethan Laird','details':{'number':27,'age':21,'position':'Defender','height':1.77}},
             {'name':'Sinclair Armstrong','details':{'number':30,'age':19,'position':'Striker','height':1.82}},
             {'name':'Joe Walsh','details':{'number':32,'age':20,'position':'Goalkeeper','height':1.91}},
             {'name':'Albert Adomah','details':{'number':37,'age': 34,'position': 'Midfielder','height':1.85}},
             {'name':'Tim Iroegbunam','details':{'number':47,'age':19,'position':'Midfielder','height':1.86}}]

#accessing a value in dictionary
print('Age of Indexed Player:',qpr_squad[4]['details']['age'])

#list and dictionary comprehension
old_players = [player for player in qpr_squad if player['details']['age'] >30]
old_player_names = {n['name']:n['details']['age'] for n in old_players}
print('Players Above 30:',old_player_names)

#converting a list of dictionaries into a dictionary into a list
dict_of_names = {n['name']:n['details']['age'] for n in qpr_squad}
keys_names = dict_of_names.keys()
value_names = dict_of_names.values()
list_of_names = list(keys_names)
list_of_ages = list(value_names)
print('List of Player Names:',list_of_names)
print('List of Player Ages:', list_of_ages)

#splitting list to only pick up the first name. Indexing[0] for first name. split method uses space as seperator.
last_names = [name.split()[1] for name in list_of_names]
print('Player Surnames:',last_names)


#using the reduce function to sum the values in a list. lambda is described function
from functools import reduce
sum_of_ages = reduce(lambda add, up: add + up,list_of_ages)
print('Sum of Player Ages:',sum_of_ages)

#using the reduce function and filtering and mapping
total_ages_midfielders = reduce(lambda add, up,:add + up['details']['age'],[up for up in qpr_squad if up['details']['position']=='Midfielder'],0)
print('Sum of Midfielder Ages:',total_ages_midfielders)



