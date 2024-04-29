# # name = input("Enter your name: ")
# # color = input("Enter your favourite color: ")
# # print(name + " likes " + color)

# # birth_year = input("Birth Year: ")
# # age = 2024 - int(birth_year)
# # print(type(age))
# # print(age)

# weight = int(input("Enter the weight in gram: "))
# result = weight/1000
# print(result)
# import nltk
# print ("Python and NLTK installed succesfully")

# course = '''Python for Begineers,
# Like, share and subscribe'''
# another = course[:]
# print(another)
# print(course[0:3]) #print from 0 to 2, excludes 3
# print(course[-1]) #print the last character
# print(course[:3]) #print from 0 to 2, similar to first
# print(course[5:]) #print from 5th character to all
# print(course[:]) #print from 0 character to last character
# print(course[1:-1]) #print from 1st character to -2th character, excluding -1

#FORMATTED STRING
# first = "Bhupendra"
# last = "Badal"
# msg = f'{first} [{last}] is a coder'
# print(msg)

#STRING METHODS
# course = 'Python for Beginners'
# print(len(course)) #print the length
# print(course.upper()) #print in uppercase
# print(course.lower()) #print in lowercase
# print(course.find("B")) #used to find
# print(course.replace('Beginners',"Absolute Beginners")) #replace the character
# print('Python' in course) #in is used for boolean value

#ARITHMETIC OPERATIONS
# print(10 ** 3) #10 to the power 3
# print(10 * 3) #10 time 3
# x = 10
# x = x + 3 #Assignment operator
# x -= 3 #Augmented assignment operator
# print(x) #the value of x will be the last value assigned to x

# ORDER
# parenthesis
# exponential power
# multiplication or division
# addition or substration

#MATH FUNCTION
# import math
# print(math.ceil(2.9)) 
# x = 2.9
# print(round(x)) #round off to the nearest value

#IF STATEMENT
# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Enjoy your day")
# elif is_cold:
#     print('''It's not hot. 
# Wear warm clothes.''')
# else:
#     print("Its lovely day.")
# price = 1000000
# good_credit = False
# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: {down_payment}$")

#   LOGICAL OPERATOR
# 1 - LOGICAL OPERATOR
# has_high_income = True
# has_criminal_record = False

# if has_high_income or not has_criminal_record:
#     print("Eligible for loan")

# 2 - COMPARISON OPERATOR
# temperature = 30
# if temperature != 30:
#     print("It's a hot day.")
# else:
#     print("It's not a hot day.")

# name = "BHUPENDRA"
# if len(name) < 3:
#     print("Name must be atleast 3 characters.")
# elif len(name) > 50:
#     print("Can be a maximum of 50 characters.")
# else:
#     print("Name looks good.")

# weight = int(input("Weight: "))
# unit = input('(L)bs or (K)g:')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds.")


# WHILE LOOP
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")
        
# GUESSING GAME
# secret_number = 9
# guess_count = 0
# while guess_count < 3:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print('Hurrey, You won!!')
#         break
# else:
#     print("Sorry, Try Again!")

#CAR GAME
# i = "help"
# print("WELCOME TO THE CAR GAME")
# start = input("> ")
# while start == 'help':
#     choice = str(input('''start - to start the car
# stop - stop the car
# quit - to exit '''))
#     if choice == "start":
#         print("Car started...")
#         break
#     elif choice == "stop":
#         print("The car is stopped.")
#         break
#     elif choice == "quit":
#         print("GAME END")
# else:
#     print("wrong command.")
        
# FOR LOOPS
# for item in 'Python':
#     print(item)

# for item in ['Bhupendra', 'John', "Sarah"]:
#     print(item)
# for item in [1, 2, 3, 4]:
#     print(item)

# for item in range(10): #from 0 to 10
#     print(item)
# for item in range(5, 10): #from 5 to 10
#     print(item)

# prices = [10, 20 ,30]
# total = 0
# for item in prices:
#     total += item
# print(f"Total: {total}")
    
# NESTED LOOP
# numbers = [5, 2, 5, 2 ,2]
# for count in numbers:
#     print('*' * count )

# numbers = [5,2,5,2,2]
# for count in numbers:
#     output = ''    
#     for count in range(count):
#         output += '*'
#     print(output)  

#

#Exception handling
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError:
#     print("Invalid Value")