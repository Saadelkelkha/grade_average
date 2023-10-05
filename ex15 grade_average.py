A=float(input("type the first note :"))
B=float(input("type the second note :"))
C=float(input("type the third note :"))
while A<0 or A>20 :
    A=float(input("type in the first note a number between 0 and 20 : "))
while B<0 or B>20 :
    B=float(input("type in the second note a number between 0 and 20 : "))
while C<0 or C>20 :
    C=float(input("type in the third note a number between 0 and 20 : "))
M=(A+B+C)/3
if M>=16 :
    print("very good")
elif M>=14 and M<16 :
    print("good")
elif M>=12 and M<14 :
    print("fairly good")
elif M>=10 and M<12 :
    print("fair")
else :
    print("unsatisfactory")
print("the average grade is",M)