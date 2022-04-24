""" Working with Lists with for loop """

subjects=["Hindi","Python","Java","DSA","Networking","DME","SM"]

#traversing elements of the list with range function
#print("Range Function used!! ")
#size=len(subjects) #saving the len of the list
#for subject in range(size): #subjects=["Hindi","Python","Java","DSA","Networking","DME","SM"]
#        print(subjects[subject])

#traversing the elements of the list without having range function
#print()#print new line
#syntax for element in list_name:
#           print(element)

for subject in subjects:  #subjects=["Hindi","Python","Java","DSA","Networking","DME","SM"]
    print(subject)


""" working on Dictionaries with for loop """

record={"Hindi":79,"Python":99,"Java":95,"DSA":88,"Networking":84,"DME":65,"SM":65}

#to print a single element with the key 
#print(record["Hindi"])

#print the key names of the dictionary
print(record.keys())

#print the value of the dictionary

print(record.values())

#print both but with the specif function
print(record.items())

#printing the whole dictionary
print(record)

#printing the key elements form a dictionary

for name in record.keys():
    print(name.upper())
    #printing values with keys
    print("printing the value with key, " ,record[name])

#printing the value elements form a dictionary

for name in record.values():
    print(name)

#printing elements form dictionary with keys and values 
for key,value in record.items():
    print(key,value)