# Q2. WAP to check if a  list contains a plindrome of elements.

# list=[1,2,3,2,1]
list = ["m","a","a","m"]

newlist=list.copy()
newlist.reverse()

if(list == newlist):
    print("Palindrome")
else :
    print("not palindrome")