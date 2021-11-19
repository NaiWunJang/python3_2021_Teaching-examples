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
car = ["Maybach","Lexus","Mazda","Ford","Lexus","Toyota"]
car.extend(lucky_numbers)
#car.append("Honda")
print(car)
car.append("Honda")
print(car)
car.insert(1,"BMW")
print(car)
car.remove("Toyota")
print(car)
#car.clear()      #All Clear,and can impact after program!!!
#print(car)
car.pop()
print(car)
print(car.index("BMW"))
print(car.count("Honda"))
print(car.count("Lexus"))
###########################################################
lucky_numbers =[7,77,777,7777,77777,777777]
car = ["Maybach","Lexus","Mazda","Ford","Lexus","Toyota"]
car.sort()
print(car)
lucky_numbers.sort()
print(lucky_numbers)
############################################################
lucky_numbers =[9,46,2,4,12,45,665,]
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers =[9,46,2,4,12,45,665,]
lucky_numbers.reverse()
print(lucky_numbers)
car2 =car.copy()
print(car2)
############################################################
################ Tuples ####################################
############################################################
