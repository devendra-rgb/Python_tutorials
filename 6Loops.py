""" using of for loops with the help of range function to print numbers"""

for i in range(10):
    print(i*2)
    
#print("All elements are printed")    


#Working with  lists 

guests=["Virat","Dohni","Dinesh Karthik","Naveen","Devendra"]

#print("Welcome to the party "+ guests[0])
#print("Welcome to the party "+ guests[1])
#print("Welcome to the party "+ guests[2])
#print("Welcome to the party "+ guests[3])
#print("Welcome to the party "+ guests[4])

#traversing through list
#insted of manually writing we can use for loop to print  all statements 
for i in range(len(guests)):
    print("Welcome to the party "+ guests[i].upper())

Name="Naveen "
for i in range(len(Name)):
    print(Name[i])

for num in range(1,100,2):
    print(num)