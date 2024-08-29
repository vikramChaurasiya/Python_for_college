list = [2, 1, 3]

list.append(4) #adds one element at the end [2,1,3,4]
list = [2, 1, 3]

# list.insert( idx, el ) insert element at index

# in list String is also use sort() methode for sort string element.  

list.sort( ) #sorts in ascending order [1,2,3,4]

list.reverse( ) #reverses list
list.sort( reverse=True ) #sorts in descending order [4,3,2,1]

print(list)

# Remove methode 

lst = [2,1,3,1]
lst.remove(1) # remove element at index no.
print(lst)
lst.pop(0) # it is same as remove methode
print(lst)
