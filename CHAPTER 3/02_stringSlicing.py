# slicing strings

greeting="Good Morning"
name="vaibhav"
print(type(name))
print(greeting+name)


# creting a variable c with greeting+name
c=greeting+ name
print(c)



# to get part of strings
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

# you cannot change name[0]
# name[3]="i"

# slicing gives name[x:y] gives from x to y-1
print(name[0:3]) 


# using negative indexes: this is used if length is unkonown you can access last elemnt of string using name[-1]
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])


# if y is not given it takes default as equal to length of string
print(name[0:])  

# if x is not given it gives default as 0
print(name[:7])


# this is same as name[4:7]
c=name[-4:-1]  
print(c)

# skiping characters while slicing
# put 3 parameter as skipped
nm="vaibhavnangia"
d=nm[0:13:2]
print(d)