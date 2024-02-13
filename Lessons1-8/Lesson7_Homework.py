# Завдання 1:
# Напишіть функцію, яка виводить на екран відформатований текст, зазначений нижче:
# “Don't let the noise of others'
#     opinions drown out your
#             own inner voice.”
#                     Steve Jobs
#
def get_text():
    text=("`Dont let the noise of others\n opinions drown out your \nown inner voice.` \n Steve Jobs")
    new_text=text.replace("\n"," ")
    print(new_text)
get_text()

# Завдання 2:
# Напишіть функцію, яка приймає два числа в якості параметрів та виводить всі непарні числа між ними.

# def get_numbers(num1,num2):
#     for x in range(num1,num2):
#         if x%2 != 0:
#             print(x)
# get_numbers(1,34)

# Завдання 3:
# Напишіть функцію, яка виводить горизонтальну або вертикальну лінію з певного символу.
# Функція приймає в якості параметрів: довжину лінії, напрямок та символ.

# def get_line():
#     try:
#         length = int(input("Type lenth"))
#         side = int(input("Type side. 1-rigth, 2-down"))
#         symbol = input("Type symbol")
#         if side == 1:
#             print(symbol * length)
#         elif side == 2:
#             x = 0
#             while x < length:
#                 print(symbol + "\n")
#                 x=x+1
#     except ValueError:
#         print("Try again and use only digits")
#     except IndexError:
#         print("Try again and use only digits")
#     except UnboundLocalError :
#         print("Its UnboundLocalError")
#
# get_line()

# Завдання 4:
# Напишіть функцію, яка повертає максимальне з чотирьох чисел. Числа передаються як параметри.
#

# def get_max(num1,num2,num3,num4):
#     max_num=str(max(num1,num2,num3,num4))
#     print("Max number is "+max_num)
# get_max(23,-66,88,0)

# Завдання 5:
# Напишіть функцію, яка повертає суму чисел у вказаному діапазоні.
# Межі діапазону передаються як параметри.
#

# def get_summ(num1,num2):
#     try:
#         sum=0
#         for x in range ( num1,num2+1):
#             sum=sum+x
#             print(x,sum)
#         print(sum)
#     except ValueError:
#         print("Try again and use only digits")
#     except IndexError:
#         print("Try again and use only digits")
# get_summ(2,6)


# Завдання 6:
# Напишіть функцію, яка перевіряє, чи є число простим. Число передається як параметр.
# Якщо число просте, поверніть true, інакше false.
#
# def isSimple():
#     try:
#         number=int(input("Type number"))
#         if number%3==0 or number%5==0 or number%2==0:
#             print("This number is not simple: "+str(number))
#         else:
#             print("This number is simple: " + str(number))
#     except ValueError:
#         print("Try again and use only digits")
#     except IndexError:
#         print("Try again and use only digits")
# isSimple()

# Завдання 7:
# Напишіть функцію, яка перевіряє, чи є шестизначне число "щасливим". Число передається як параметр.
# Якщо число щасливе, поверніть true, інакше false. "Щасливе шестизначне число" - це число,
# у якого сума перших трьох цифр дорівнює сумі трьох наступних цифр.
# Наприклад, 123420 - щасливе (1+2+3 = 4+2+0), а 723422 - нещасливе (7+2+3 ≠ 4+2+2).

# def isLuckyNumber():
#     try:
#         number = input("Type number with 6 digits")
#         sum = 0
#         for x in range(0, 3):
#             sum = sum + int(number[x])
#         print(sum)
#
#         if sum == int(number[3]):
#             print("Its Lucky number")
#         else:
#             print("Try again")
#     except ValueError:
#         print("Try again and use only digits")
#     except IndexError:
#         print("Try again and use only digits")
#
#
# isLuckyNumber()
