# Week4. Task1 ----> Atabek
# 1)
# def last_number() :
#     num = input ('Введите число : ')
#     num = str(num)
#     print (num[-1])
# last_number()

# 2)
# def chetnoe():
#     num = int(input('Enter a number: '))
#     if num % 2 == 0:
#         print('Chetnoe')
#     elif num % 2 != 0:
#         print('Ne chetnoe')
# chetnoe()

# 3)
# def kvadrat():
#     number = input('Enter your number: ')
#     square = []
#     for i in range (int(number)):
#         i= i**2
#         square.append(str(i))
#     print(','.join(square))
# kvadrat()

# 4)
# def polindrom():
#     slovo =input('Enter your word: ')
#     if slovo [::-1] == slovo:
#         print('Your word is polindrom!')
#     else:
#         print('Your word is not polindrom!')
# polindrom()

# 5)
# import datetime
# def date_check():
#     day = int(input('Enter the day: '))
#     month = int(input('Enter the month: '))
#     year = int(input('Enter the year: '))
#     try:
#         dataa = datetime.date(year, month, day)
#         print(dataa)
#         print(True)
#     except:
#         print('Incorrect!!!')
# date_check()

# 6)
# def three_nums():
#     num = input('Type the трехзначное число: ')
#     if len(num) < 3 or len(num) > 3:
#         raise ValueError ('I said only трехзначное число!!!')
#     num = str(num)
#     print (int(num[0]) + int(num[1]) + int(num[2]))
# three_nums()

# 7)
# def numbers():
#     num = input('Enter your number: ')
#     num = str(num)
#     print('Kolichestvo razryadov: ' + str(len(num)))
# numbers()

# 8)
# def max_chislo():
#     nums = []
#     san = -1
#     while True:
#         try:
#             d = input('("EXIT for leave") Enter your number: ')
#             if d == 'EXIT':
#                 print('The maximum number: ' + san)
#                 break
#             nums.append(d)
#             for i in nums:
#                 if int(i) > int(san):
#                     san = i
#         except ValueError:
#             raise TypeError ('Sorry, only numbers!!!')
# max_chislo()
# TASK8 EXTRA-----:::::::::::-------
# def max_chislo_1():
#     list_ = [4, 5, -67, 15, 64, -86, 2475, 9485204839, 98436908, 94, 6, -94958]
#     max_ = 0
#     min_ = 0
#     for i in list_:
#         if i > max_:
#             max_ = i
#         if i < min_:
#             min_ = i
#     print('Maximum number is: ' + str(max_) + ' ' + 'and'+' ' + 'Minumum number is: ' + str(min_))
# max_chislo_1()

# 9)
# def cal():

#     try:
#         operatsiya = ['+', '-', '*', '/']
#         opera = input ('| + | - | * | / | ')
    
#         while opera not in operatsiya :
#             raise TypeError ('OMG INCORRECT OPERATIONS!!')
#             opera = input ('| + | - | * | / | ')

#         num1 = input ('Enter your first number : ')
#         num2 = input ('Enter your second number : ')

#         if opera == '+' :
#             res = int(num1) + int(num2)
#             print(f'Your answer is : {res}')

#         elif opera == '-' :
#             res = int(num1) - int(num2)
#             print(f'Your answer is : {res}')

#         elif opera == '*' :
#             res = int(num1) * int(num2)
#             print(f'Your answer is : {res}')

#         elif opera == '/' :
#             res = int(num1) / int(num2)
#             print(f'Your answer is : {res}')  
#     except ZeroDivisionError :
#         raise TypeError ('Dividing to ZERO prohibited !!!')   

#     except ValueError :
#         raise TypeError ('OMG you so weird, I said only freaking NUMBERS !!!')   

#     finally :
#         print('BYE, and have a good one!')

# cal()

# 10)
# def countingValleys(steps, path):
    
#     levels = 0
#     valleys = 0
#     for i in path:
#         if i == "U":
#             levels += 1
            
#             if levels == 0:
#                 valleys += 1
#         else:
#             levels -= 1
             
#     return valleys

















