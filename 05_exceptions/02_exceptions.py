def divide():
    try:
        op1 = float(input("Set the first number: "))
        op2 = float(input("Set the second number: "))
        print(f"The result of division is {str(op1 / op2)}")
    except ValueError:
        print("The value setted is incorrect")
    except ZeroDivisionError:
        print("It cant be divided by 0")

    print("Finished")


if __name__ == '__main__':
    divide()
