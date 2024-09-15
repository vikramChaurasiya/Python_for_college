# Some Dictionary methods 

student = {
    "name":"karn chaurasiya ",
    "subject" : {
        "phy" :97,
        "chem" : 98,
        "math" :95
    }
}

# 1st dict.keys():- return all keys cllection.

print(student.keys()) # only one dict return all keys 

# how to find dictionary length 
print(len(student)) #1st methode claculate length

print(list(student)) # typecasting in list.

print(len(list(student.keys()))) #2nd methode calculate length

# 2nd dict.values() :- returns all values collection.

print(student.values())

# 3rd dict.items():- return all (key,pair) pairs as tuples.

print(student.items())

# if want only one pair then 
pairs = list(student.items()) #typecast in list then

print(pairs[1]) #only needed pair access.

# 4th dic.get("key"):- returns the key according to value.

print(student.get("name")) #if any key not define then it is not create error only print None.

print(student["name"]) #if any key not define then it is create error.

# 5th dict.update(newDict):- insert the specified items to the dicitionary.

student.update({"city" : "dbg"})
print(student)