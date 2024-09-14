# nested dictionary
# how to create a nested dictionary
student = {
    "name":"karn chaurasiya ",
    "subject" : {
        "phy" :97,
        "chem" : 98,
        "math" :95
    }
}

print(student) # print dict 
print(student["subject"]) # nested dict print only
print(student["subject"]["chem"]) #acess nested element acess.

