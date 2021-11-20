print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")
###########################################################################
character_name = "Will"
character_age = "21"
is_male = True
print("My name is " + character_name + "")
print("He is " + character_age + " years old. ")
############################################################################
character_name = "Lee"
print("He best friend is " + character_name + ".")
print("Hello World")
print("Hello\nWorld")
print("Hello\"world\"")
###########################################################################
Will = "Will Jang"
print(Will + " is cool ")
print(Will.lower())
print(Will.upper())
print(Will.isupper())
print(Will.islower())
print(Will.upper().isupper())
print(len(Will))
print(Will[0])
print(Will[3])
print(Will[4])
print(Will[5])
print(Will.index("i"))
print(Will.index("Ja"))
print(Will.replace("Will", "Willism"))
print(1)
print(1.61843)
print(-1.61843)
print(1.61843 * (2 +3))
print(10 / 3)
print(10 % 3)
my_num = 7
print(my_num)
print(str(my_num))
print(str(my_num) + " is my favorite number !")
##########################################################################
my_num = -7
print(abs(my_num))
print(pow(3,2)) # 3 square 2
print(pow(1.61843,2.71828))
print(max(1.61843,2.71828))
print(min(1.61843,2.71828))
print(round(1.61843))
print(round(1.1843))
############################################################################
from math import *
print(floor(7.7))
print(ceil(7.7))
print(sqrt(49))
############################################################################
name = input("Please enter your name : ")
age = input("Please enter your age : ")
print("Hello " + name + "! You are " + age + " years old." )
#################################### 2021/11/18_edit
num1 = input("Enter a number : ")
num2 = input("Enter another number : ")
result = num1 + num2
print(result)
print(int(result))
result = float(num1) + float(num2)
print(result)
color = input("Enter a color : ")
car = input("Enter a car brand : ")
####################################
print("My car is " + color)
print(car + " is my car trademark.")
####################################
#### List ##########################
####################################
car = ["Maybach","Lexus","Mazda","Ford","Toyota"]
print(car,car[1],car[1:3])
####################################
#### List Functions ################
####################################
lucky_numbers =[7,77,777,7777,77777,777777]
car = ["Maybach","Lexus","Mazda","Ford","Toyota"]
car.extend(lucky_numbers)
print(car)
