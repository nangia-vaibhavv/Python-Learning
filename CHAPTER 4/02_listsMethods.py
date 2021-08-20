# writing this gives me none because this sorts the actual list
# which is not valid         

# l1=[1,8,7,2,21,15]
# l1_sorted=l1.sort()

# print(l1_sorted)

l1=[1,8,7,2,21,15]

# prints orignal list
print(l1)   

# prints sorted list
l1.sort()
print(l1)

# prints list in sorted order
l1.reverse()
print(l1)

# add to the end of the list
l1.append(1000)
print(l1)

# insert(index,value)
l1.insert(1,5444)
print(l1)

# removes element at that index
l1.pop(2)
print(l1)

# removes 5444 from list if present
l1.remove(5444)
print(l1)

