# take user input as list of marks he would like to have in his breakfast

# typecast input funtion to int an not in string
m1=int(input("Enter Marks for student Number 1 : "))
m2=int(input("Enter Marks for student Number 2 : "))
m3=int(input("Enter Marks for student Number 3 : "))
m4=int(input("Enter Marks for student Number 4 : "))
m5=int(input("Enter Marks for student Number 5 : "))
m6=int(input("Enter Marks for student Number 6 : "))

myList=[m1,m2,m3,m4,m5,m6]
myList.sort()
print(myList)