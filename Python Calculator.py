running = True 
print("============================")
while running:
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exit program")
    cmd = int(input("Enter number : "))
    if cmd == 1:
        print("============================")
        print("Addition")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first + secund
        print(first ,'+' ,secund ,'=' , result)
        print("============================")
    elif cmd == 2:
        print("============================")
        print("Subtraction")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first - secund
        print(first ,"-" ,secund ,"=" , result)
        print("============================")
    elif cmd == 3:
        print("============================")
        print("Multiplication")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first * secund
        print(first ,"*" ,secund ,"=" , result)
        print("============================")
    elif cmd == 4:
        print("============================")
        print("Division")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first / secund
        print(first ,"/" ,secund ,"=" , result)
        print("============================")
    elif cmd == 5:
        print("============================")
        print("Quit!")
        running = False
