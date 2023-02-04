def do_op(num1, num2, op):
    sum = 0
    num1 = float(num1)
    num2 = float(num2)
    if op == "+":
        sum = num1 + num2
    elif op == "-":
        sum = num1 - num2
    .
    .
    return sum

op = "oppa"
total = 0
while op != "=":
    num1 = input("enter first number: ")
    op = input("ener operation: ")
    num2 = input("enter next number: ")
    total = do_op(num1, num2, op)

print("Total is {}".format(total))