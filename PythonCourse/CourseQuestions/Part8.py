#importing modules for type annotation list and tuple

#Union means that the type annotation will return something or 'None'

#def function_1(number: Union[str, None]) #can use a string or none in function

n = 81
sqroot = n**(1/2)
print(sqroot)

#importing a previously made module (py file) which contains a function
import mymodule
print(mymodule.greeting('richie'))
