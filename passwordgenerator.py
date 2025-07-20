#using lists,forloop,if statement:
student_scores =[1,2,2,34,2,345,567,8970,9358]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)


#for loop and using the range() function(range is lyk conjunction)
#for number in range(a,b):   print(number)

for number in range(1,10):
    print(number)
#if u wanna add the last number in the output u should enter 11 not 10)
    
total = 0
for number in range(1,101):
    total += number
print(total)

#creating a password generator

import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','t','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['#','*','+','!','(',')','&','+']

print("Welcome to the password generaor!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many symbols would you like?\n"))
nr_symbols = int(input("How many numbers would you like?\n"))

#easy level


password = ""
#nr_letters = 4
for char in range(1, nr_letters + 1):
    #that is 1 to 4
    #random_char = random.choice(letters)     password += random_char      print(password)
    password += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

#here lyk(1,nr_letters + 1) u can also type it as (0, nr_letters)

print(password)


#hard level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range (0,nr_numbers):
    password_list.append(random.choice(numbers))

for char in range (0,nr_symbols):
    password_list.append( random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is : {password}")






    
    






 
