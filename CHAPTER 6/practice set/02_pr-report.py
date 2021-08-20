# take student mrks , if any subject is less than 33 he fails, or if total is less than 40 he fails else congo

sub1=int(input("enter first subject\n"))
sub2=int(input("enter second subject\n"))
sub3=int(input("enter third subject\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("better luck next time , less than 33 marks")

elif((sub1+sub2+sub3)/3<40):
    print("sorry, total is iss than 40")
else:
    print("congo")        