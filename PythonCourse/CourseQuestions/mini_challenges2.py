
def ordinal_suffix(number:int) ->str:
    if number % 100 in [11,12,13]:
        x = 'th'
    elif number % 10 == 1:
        x = 'st'
    elif number % 10 == 2 and number <1000:
        x = 'nd'
    elif number % 10 == 3 and number <1000:
        x = 'rd'
    elif number >= 0:
        x = 'th'
    else: raise ValueError('Invalid Value Provided')
    return str(number) + x

print(ordinal_suffix(12))