""" Sets """

data={'orange','apple','orange'}

print(data)

#checking the datatype with type function

print(type(data))

#adding elements to the set by update function which will take a list as a parameter 
data.update(["pineapple","cherry",1,'orange'])

print(data)

#removing elements form the set data type with remove() function
data.remove('orange')

print(data)

print(len(data))




""" 
anagram 

Listen   Silentz

name 1= Naveen

name 2= Devendra 

"""
#how anagaram working

name={1}

name.update('listen'.lower())
print("len of the name" ,len(name))

name.update('apple'.lower())

print("len of the name after updating " ,len(name))

#frozing the set
company=frozenset(data)

print(company)


a={1}
b={1}

a.update('listen') #updating an data with single 

b.update(['listen']) #updating datay with list

print(a,b)