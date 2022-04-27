a=7
b=6

""" conditional statements """
#to find two variables are equal or not with "==" symbol
print(a == b)
#comparing variables
print(a>b)

print(a<b)

#Not equal to 
print(a != b)

#greater than or equal , Less than or equal

print(a >= b)

print(a <= b)

nums=[1,2,3,4,5,6]

#to check it is in list 

print( 7 in nums )

#to check it is not in list

print(7 not in nums)

#devendra and  naveen 

#devndra or naveen


#using and operator

print( 7>6 and 6<7 )

print( 7<6 and 6<7 )


#using or operator

print(7<6 or 6<7)

print(True and False)

#using logical operator with strings
print('Devendra'=='Devendra')

#using the if 
if 7<= 6 :
    print("7 is greater than 6")
else:
    print("7 is not greater than 6")


""" modulo % to find the remainder  """
print(50 % 2 )


if 5%2 == 0 :
    print("5 is even ")
else:
    print("5 is odd")

numbers=[1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    print(i)

#to print even numbers with if condition
for i in numbers:
    if i % 2 == 0:
        print(i)
    else:
        print()