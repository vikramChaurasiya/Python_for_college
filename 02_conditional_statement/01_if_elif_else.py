# Syntax 

# if(cond):
#     statement
# elif(cond):
#     statement1
# else
#     statement


# in python multiple statement you can wirte then follow indentation.
# indentation means one tab space.

# only if

age =55

if(age>=18):
    print("can vote")
    
# if ,elif 

light = "green"
if(light =="red"):
    print("stop")
elif(light =="green"):
    print("go")
elif(light =="yellow"):
    print ("look")


# if,elif,else

if(light =="red"):
    print("stop")
elif(light =="green"):
    print("go")
elif(light =="yellow"):
    print ("look")
else:
    print("light is broken")


marks = 88
if(marks >=90):
    print("Grade A")
elif(marks >=80 and marks <90):
    print("Grade B")
elif(marks >= 70 and marks <80):
    print("Grade C")
else :
    print("Grade D")