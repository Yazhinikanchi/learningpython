6number= ["1","3","5","7","9","0"]
key= input("enter the value to be searched")
n = len(number)
for i in range (0,n):
    if(number [i] == key):
        print ("element found at index:",i)
        break;
else:
    print("element not found")







