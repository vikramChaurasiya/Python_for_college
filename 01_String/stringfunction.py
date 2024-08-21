# String function
# str.endswith("ege"):-> this function check string is true or false.

str ="apna college"
print(str.endswith("ege"))

# capitalize():-this function check first letter is Capitial or not .
# capitalize () not change original string.

print(str.capitalize())

# if you to change original string then you can

str =str.capitalize()
print(str)


# .replace(old,new):-> this function is replace old String to new String for examle:-

print(str.replace("e" ,"s"))

# .find(word) ;-> this function is search word and return index of string if not search index then return -1.

print(str.find("c"))

# .count(" "):->  this function count how many times of this word is exits.

print(str.count("e"))
