
#sorted function with input & output

print(sorted(input("input here:")))

# defining your own function using def. reverse is name of function and text is variable name inside function
def reverse(text) :
    return text[::-1]

#using the created function
print(reverse("hungary"))

def counting_first_letter(words,letter) :
    occurance = 0 #this is used to count. occurance = 0 unless more counted
    for word in words : #this is for loop. word is the variable in words that it goes through one at a time
        if word.startswith(letter) :
            occurance += 1 #+= means occurence = occurence +1
    return occurance

print(counting_first_letter(['apple','chair','table','anaconda'],'a'))

for even_numbers in range(0,100,10) : #using for loop with range. start, stop, step.
    print(even_numbers)
count=0
while count <5 : #using while loop - when boolean value is met
    count+=1
    print(count)

print(locals())