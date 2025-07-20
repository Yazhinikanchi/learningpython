#1ST PROGRAM
x=int(input("enter a number:"))
y=int(input("enter a number:"))
temp=x
x=y
y=temp
print("the value of x after swapping:",x)
print("the value of y after swapping:",y)



#2nd program
A=[1,2,3,4,5]
n=len(A)
for i in range(0,n):
    B=A[i+1:]+A[:i+1]
    print("Circulation",i+1,B)

    

#3RD PROGRAM
import math
p1=[4,0]
p2=[6,6]
distance=math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print(distance)



#5TH PROGRAM
x=int(input("Enter a nummber:"))
i=1
while i<=x:
    if (i%2==0):
        print(i,end=" ")
    i=i+1







