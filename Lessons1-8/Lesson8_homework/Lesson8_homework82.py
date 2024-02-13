# #task 1

# def sum_func(num1,num2,num3):
#     return num1+num2+num3
#
# def mult_func(num1,num2,num3):
#     return num1*num2*num3
#
# # print(sum_func(num1,num2,num3))
# mult_func(22,22,666)
# # print()


# print("Sum = "+str(sum))
# print("Multiplication is "+str(mul))

# task2
# Завдання 2
# Користувач вводить три цифри з клавіатури.
# Залежно від вибору користувача програма виводить на екран
# максимум із трьох, мінімум із трьох або середнеарифметичне трьох чисел.

# def find_max(num1,num2,num3):
#     a=num1
#     if num2>num1:
#         a=num2
#     if num3>num2:
#         a=num3
#     return a
#
# print(find_max(5,-89,87))

# Завдання 3
# Користувач вводить з клавіатури номер дня тижня
# (1-7). Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, то на екрані напис понеділок, 2 - вівторок і т.д.

# def type_num(day):
#     if day==1:
#         return "Its Monday"
#     elif day==2:
#         return "Its Tuesday"
#     elif day==3:
#         return "Its Wednessday"
#     elif day==4:
#         return "Its Thursday"
#     elif day==5:
#         return "Its Friday"
#     elif day==6:
#         return "Its Saturday"
#     elif day==7:
#         return "Its Sunday"
#     else:
#         return "Number should be between 1 and 7"
# type_num(6)

# task 4
# Користувач вводить з клавіатури номер місяця (1-12).
# Необхідно вивести на екран назву місяця.
# Наприклад, якщо 1, то на екрані напис січень,
# 2 - лютий і т.д.


# def type_month(month):
#     if month==1:
#         return "Its January"
#     elif month==2:
#         return "Its February"
#     elif month==3:
#         return "Its March"
#     elif month==4:
#         return "Its April"
#     elif month==5:
#         return "Its May"
#     elif month==6:
#         return "Its June"
#     elif month==7:
#         return "Its July"
#     elif month==8:
#         return "Its Aughust"
#     elif month==9:
#         return "Its September"
#     elif month==10:
#         return "Its October"
#     elif month==11:
#         return "Its November"
#     elif month==12:
#         return "Its December"
#     else:
#         return "Number should be between 1 and 12"

# #task 5
# Користувач вводить із клавіатури число. Якщо число
# більше нуля потрібно вивести напис "Number is positive",
# якщо менше нуля "Number is negative", якщо дорівнює нулю
# «Number is equal to zero»

# def number(number):
#     if number>0:
#         return "Number is bigger than 0"
#     elif number==0:
#         return "Number is 0"
#     else:
#         return "Number is less then 0"


# task6
# Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні,
# вивести їх на екран у порядку зростання

# def numbers(num1, num2):
#
#     if num2==num1:
#         return "They are the same"
#     else:
#         if num1>num2:
#             return str(num2)+" , "+str(num1)
#         else:
#             return f"{num1} , {num2}"
#
# print(numbers(6,4))
# Завдання 7
# Користувач вводить з клавіатури два числа
# (початок та кінець діапазону). Потрібно проаналізувати
# всі числа в цьому діапазоні за таким правилом: якщо
# число кратно 7 його треба виводити на екран.

# def numbers(num1,num2):
#     for i in range(num1, num2+1):
#         if i%7 ==0:
#             return i
# print(numbers(1,8))
# Завдання 8
# Користувач вводить з клавіатури два числа (початок та кінець діапазону).
# Потрібно проаналізувати все числа у цьому діапазоні.
# Потрібно вивести на екран:
# 1. Усі числа діапазону;

# def numbers(num1, num2):
#     list1=list()
#     for i in range(num1, num2+1):
#         list1.append(i)
#     return list1
# print(numbers(2,7))

# Завдання 8
# 2. Усі числа діапазону у спадному порядку;
# def numbers(num1, num2):
#     list1 = list()
#     i = num2
#     while (i >= num1):
#         list1.append(i)
#         i = i - 1
#     return list1
# print(numbers(2, 7))


# Завдання 8
# 3. Усі числа, кратні 7;
# def numbers(num1, num2):
#     list1=list()
#     for i in range(num1, num2+1):
#         if i%7 ==0:
#             list1.append(i)
#     return list1
# print(numbers(1,15))

# Завдання 8
#    4. Кількість чисел, кратних 5.
# def numbers(num1, num2):
#     list1=list()
#     a=0
#     for i in range(num1, num2+1):
#         if i%7 ==0:
#             a=a+1
#             list1.append(i)
#     return a
# print(numbers(5,100))


# Завдання 9
# Користувач вводить з клавіатури два числа
# (початок та кінець діапазону). Потрібно проаналізувати
# усі числа у цьому діапазоні. Виведення на екран має відбуватися
# за правилами, наведеними нижче.
# Якщо число кратне 3 (ділиться на 3 без залишку), потрібно вивести слово Fizz.
# Якщо число разів 5 потрібно вивести слово Buzz.
# Якщо число кратно 3 та 5 потрібно вивести Fizz Buzz.
# Якщо число не раз не 3 і 5 потрібно вивести саме число.

# def numbers(num1, num2):
#     list1=list()
#     for i in range(num1, num2+1):
#         if i % 3 == 0 and i % 5 == 0:
#             list1.append(str(i) + "Buzz Fizz")
#             continue
#         if i%3==0:
#             list1.append(str(i)+"Fizz")
#             continue
#         if i%5==0:
#             list1.append(str(i)+"Buzz")
#             continue
#         else:
#             list1.append(i)
#     return list1
# print(numbers(5,9))
