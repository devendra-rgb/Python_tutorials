"""" This program file contains all the basic functions of list """

names=[1,2.0,"Naveen",True]

print(names[0]) #indexing


print(names[1:4]) #Indexing


print(names)
names.pop() #popping last element

names.pop(1)#removing with specific indexing

#removing with the help of element
names.remove("Naveen")

print("this  in now",names)

names.append("Devendra")

print(names)

companies=["BMW", "BENZ", "AUDI"]

companies.insert(0,"Tesla") #insert at specific location

print(companies)

print(companies.index("BENZ")) #find the index number with the element value


ranks=[20,11,229,8,77]

#sorted(ranks)


print(sorted(ranks)) #sort 

print(sorted(ranks,reverse=True)) #reverse the order by setting the parameter to True


print(companies[0].upper()+" is No 1 company ") #to append it with the another string 

marks=[1,2,3]

sub_list=[33,34,13]

marks.append(sub_list) #adding sublist to a list

print(marks[-1][-2])


##aplying len function to the list

print(len(ranks))

##deleting the values form the list

new_list=["Light","Bottle"]

del new_list[0]

print(new_list)


"""
Functions used in the above program

pop()
pop(index_number)
remove()
append()
insert()
sorted()
sorted(reverse=True)
index()

"""


firstname="naveen" #not recommended

Firstname="naveen" #not recommended

firstName="naveen" #cammel

first_name="naveen" #snake












