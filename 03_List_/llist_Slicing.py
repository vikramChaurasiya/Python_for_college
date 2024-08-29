# List Slicing

# Syntax:- list_name  = [Starting_idx:ending_idx] 
# ending idx is not included.

marks = [56,90,78.9,89,]
print(marks[1:3]) #is called slicing,

# if in slicing first idx define and second idx is not define the autometic define in last idx.
# if in slicing second idx define and first idx is not define the autometic define in zero idx.

print(marks[ :3])
print(marks[ 1: ])

#in list negative indxing is allowed.
 