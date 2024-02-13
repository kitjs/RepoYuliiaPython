import culc_func as c


while True:
    num1=int(input("Enter num1:"))
    num2=int(input("Enter nym2"))
    command=str(input("Enter command:"))

    result=("")
    if command == "+":
        result=f"{num1}{command}{num2}={c.plus(num1,num2)}"
    elif command == "-":
        result=f"{num1}{command}{num2}={c.minus(num1,num2)}"
    elif command == "*":
        result=f"{num1}{command}{num2}={c.milt(num1,num2)}"
    elif command == "/":
        result=f"{num1}{command}{num2}={c.div(num1,num2)}"
    print(result)