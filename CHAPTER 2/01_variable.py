#these datatypes are determined bydefault

a="vaibhav" #string
a1='''vaibhav "nangia" '''
b=345   #int        
c=45.32  #decimal 
d=None  #determines it is used to define none

#printing variable
print(a)
print(a1)
print(b)
print(c)
print(d)

#printing datatypes automatically
#it bydefault determine by python library to defines its datatype
print(type(a))
print(type(a1))
print(type(b))
print(type(c))
print(type(d))


#arithmetic operators
print("the value of 3+4 is: ",3+4)
print("the value of 3-4 is: ",3-4)
print("the value of 3*4 is: ",3*4)
print("the value of 3/4 is: ",3/4)


#assignment operators
z=30
z+=2 # '''use any of these as required'''
print(z)


#comparison operators
x=(14>5)
print(x)

n=(14==6)
print(n)


#logical operators
bool1=True
bool2=False

print("The vaue of bool1 and bool2 is: ",(bool1 and bool2))
print("The vaue of bool1 or bool2 is: ",(bool1 or bool2))
print("The vaue of bool1 not bool2 is: ",( not bool2))


