# try:
#     print(a/b)
# except ZeroDivisionError:       #if
#     print("You can not div to zero")
# except TypeError:               #elif
#     print("Incorrect type")
# except NameError:               #elif
#     print("Add all variable")
# except :                        #else
#     print("Ops...")
# else:
#     print("Programm finish correcnly") #буде використано якщо не було помилок
# finally:
#     print("Exit")                     #буде виконано в будь-якому разі
#
#
# while True:
#     result = 0
#     try:
#         a = int(input("Type number1: "))
#         command = str(input("Enter your command "))
#         b = int(input("Type number2: "))
#
#         if command == "*":
#             result = f"{a}{command}{b}={a * b}"
#         elif command == "/":
#             result = f"{a}{command}{b}={a/b}"
#     except ValueError:
#         print("a or b is not correct, or both")
#     except ZeroDivisionError:
#         print("you can not divide to zero")
#     else:
#         print("Good work")
#     finally:
#         print(result)
####Task
while True:
    result = 0
    try:
        a = int(input("Type number1: "))
        command = str(input("Enter your command "))
        b = int(input("Type number2: "))

        if command == "*":
            result = f"{a}{command}{b}={a * b}"
        elif command == "/":
            result = f"{a}{command}{b}={a / b}"
    except: #голе виключення
        print("a or b is not correct, or both")
