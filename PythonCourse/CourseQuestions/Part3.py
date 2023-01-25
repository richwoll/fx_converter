
world_countries = {'albania':'europe', 'austria': 'europe', 'hungary':'europe','algeria':'africa','japan':'asia','mexico':'south america','australia':'oceania','usa':'north america'}

country = input('Insert Country:')
continent = world_countries[country] if country in world_countries else None


print(continent)

#.get returns a value of specified key
x = world_countries.get('albania')
print(x)

#.keys returns a list of dictionaries keys
y = world_countries.keys()
print(y)

#.values returns a list of the dictoinaries values
v = world_countries.values()
print(v)

#.update updates the dictionary with a key / value pairing
world_countries.update({'sweden':'europe'})
print(world_countries)

#creating a dictionary using dict from list of tuples
d = dict([('key', 'value'),('key1', 'value1'),('key2','value2')])
print(d)

p = d.get('key')
print(p)