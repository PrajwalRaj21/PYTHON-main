A = float(input("Enter the first number: "))
op = input("Enter the operator: ")
B = float(input("Enter the second number: "))


if op == '+':
    print(A + B)
elif op == '-':
    print( A - B)
elif  op == '*':
    print( A * B)
elif op == '/':
    print( A / B)

else:
    print("Invalid Operator")
    