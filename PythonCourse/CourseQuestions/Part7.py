#exercise1: write a function with 2 arguments

nums_1 = [4,7,3,9,1,2,2,4,8,9,0,3,4,6,5]
target_1 = 6

def function_1(nums,target):
    for num in nums:
        for nu in nums:
            if num + nu == target:
                tuple2= (nu, num)
                return tuple2

print(function_1(nums_1,target_1))

a = 5
b = 7
c = 9

if a or b > 6:
    print(a + b + c)

#leaving trailing comma creates a tuple data type
v = 4,5
print(type(v))
