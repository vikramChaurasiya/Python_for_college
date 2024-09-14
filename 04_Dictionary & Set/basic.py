# how to create a Dictionary.
# in dictionary can store string,nuber,float,boolean.
# can store also list and tuple.

info = {
    "F_name" : "Vikram",
    "L_name" : "Chaurasiya",
    "age" : 19,
    "Qualification" : "BCA",
    "University" : "Bihar university"
}

# how to print

print(info)
print(type(info))

# how to print element
print(info["F_name"])  # only one element print 

# how to replace element

info["L_name"] = "kumar"  # last name update from chaurasiya to kumar

print(info["L_name"])

# null dictionary also create for example:-

null_dic = {}

print(null_dic) # print
