#task 1
#
# num1=int(input("type number1"))
# num2=int(input("type number2"))
# num3=int(input("type number3"))
# sum=num1+num2+num3
# mul=num1*num2*num3
# print("Sum = "+str(sum))
# print("Multiplication is "+str(mul))

#task2

# num1=int(input("type number1"))
# a=num1
# num2=int(input("type number2"))
#
# num3=int(input("type number3"))
#
# if num2>num1:
#     a=num2
# if num3>num2:
#     a=num3
#
# print(a)


#task3
# day=int(input("Type number from 1 till 7"))
#
# if day==1:
#     print("Its Monday")
# elif day==2:
#     print("Its Tuesday")
# elif day==3:
#     print("Its Wednessday")
# elif day==4:
#     print("Its Thursday")
# elif day==5:
#     print("Its Friday")
# elif day==6:
#     print("Its Saturday")
# elif day==7:
#     print("Its Sunday")
# else:
#     print("Number should be between 1 and 7")

#task 4
#### How can I do it in another way?

# month=int(input("Type number from 1 till 12"))
#
# if month==1:
#     print("Its January")
# elif month==2:
#     print("Its February")
# elif month==3:
#     print("Its March")
# elif month==4:
#     print("Its April")
# elif month==5:
#     print("Its May")
# elif day==6:
#     print("Its June")
# elif day==7:
#     print("Its July")
# elif day==8:
#     print("Its Aughust")
# elif day==9:
#     print("Its September")
# elif day==10:
#     print("Its October")
# elif day==11:
#     print("Its November")
# elif day==12:
#     print("Its December")
# else:
#     print("Number should be between 1 and 12")

# #task 5
# Користувач вводить із клавіатури число. Якщо число
# більше нуля потрібно вивести напис "Number is positive",
# якщо менше нуля "Number is negative", якщо дорівнює нулю
# «Number is equal to zero»

# number=int(input("Type any number"))
# if number>0:
#     print("Number is bigger than 0")
# elif number==0:
#     print("Number is 0")
# else:
#     print("Number is less then 0")

#
# task6
# Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні,
# вивести їх на екран у порядку зростання

# num1=int(input("Type number 1"))
# num2=int(input("Type number 2"))
#
# if num2==num1:
#     print("They are the same")
# else:
#     if num1>num2:
#         print(str(num2)+" , "+str(num1))
#     else:
#         print(f"{num1} , {num2}. ")

# Завдання 7
# Користувач вводить з клавіатури два числа
# (початок та кінець діапазону). Потрібно проаналізувати
# всі числа в цьому діапазоні за таким правилом: якщо
# число кратно 7 його треба виводити на екран.

# num1=int(input("Type num1"))
# num2=int(input("Type num2"))
#
# for i in range(num1, num2+1):
#     if i%7 ==0:
#         print(i)

# Завдання 8
# Користувач вводить з клавіатури два числа (початок та кінець діапазону).
# Потрібно проаналізувати все числа у цьому діапазоні.
# Потрібно вивести на екран:
# 1. Усі числа діапазону;


# num1=int(input("Type num1"))
# num2=int(input("Type num2"))
#
# for i in range(num1, num2+1):
#     print(i)

    # Завдання 8
    # 2. Усі числа діапазону у спадному порядку;
# num1=int(input("Type num1"))
# num2=int(input("Type num2"))
# i = num2
# while (i >= num1):
#     print(i)
#     i = i - 1

    # Завдання 8
    # 3. Усі числа, кратні 7;
# num1=int(input("Type num1"))
# num2=int(input("Type num2"))
#
# for i in range(num1, num2+1):
#     if i%7 ==0:
#         print(i)

# Завдання 8
#    4. Кількість чисел, кратних 5.
# num1=int(input("Type num1"))
# num2=int(input("Type num2"))
# a=0
# for i in range(num1, num2+1):
#     if i%7 ==0:
#         a=a+1
#         print(i)
# print(a)


# Завдання 9
# Користувач вводить з клавіатури два числа
# (початок та кінець діапазону). Потрібно проаналізувати
# усі числа у цьому діапазоні. Виведення на екран має відбуватися
# за правилами, наведеними нижче.
# Якщо число кратне 3 (ділиться на 3 без залишку), потрібно вивести слово Fizz.
# Якщо число разів 5 потрібно вивести слово Buzz.
# Якщо число кратно 3 та 5 потрібно вивести Fizz Buzz.
# Якщо число не раз не 3 і 5 потрібно вивести саме число.

# num1=int(input("Type num1"))
# num2=int(input("Type num2"))
#
# for i in range(num1, num2+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(str(i) + "Buzz Fizz")
#         continue
#     if i%3==0:
#         print(str(i)+"Fizz")
#         continue
#     if i%5==0:
#         print(str(i)+"Buzz")
#         continue
#     else:
#         print(i)