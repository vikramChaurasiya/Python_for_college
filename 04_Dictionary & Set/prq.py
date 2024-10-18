# 1. Store following word meanings in a python dictionary:

dictionary = {
    "cat" :"a small animal",
    "table" :["a piece of furuniture", "list of facts & figures"]
}

print(dictionary)

# 2.you are given a list of subjects for students. Assume one classroom is required for 1 subject. how many classroom are needed by all students.

subject ={
    "python", "javaScript" ,"c", "c++", "python " ,"java", "c++"
}

print (subject)
print(len(subject))

# 3.WAP to enter marks of 3 subjects from the user and store them dictionary. start with an empty dictionary & add one by one. Use subject name as key & marks s value. 

marks = {}

x = int(input("enter py : "))
marks.update({"phy" : x}) 

x = int(input("enter chem : "))
marks.update({"chem" : x}) 

x = int(input("enter math : "))
marks.update({"math" : x}) 
 
print(marks)

# 4. figure out a way to store 9 & 9.0 as separate values in the set.
# (you can take help of built-in data types)

values = {
    ("float",9.0),
    ("int",9)
}

print(values)