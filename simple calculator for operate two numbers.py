# creating a calculator

num_1    = float(input("the first number: "))
operator = input("select the operator + - * /  ** : ")
num_2    = float(input("the second number: "))

if operator == "+":
    print(f"the value is {num_1+num_2}")
elif operator == "-":
    print(f"the value is {num_1 - num_2}")
elif operator == "*":
    print(f"the value is {num_1 * num_2}")
elif operator == "/":
    if num_1 == 0:
        print("0 can not divided by any number")
    else:
        print(f"the value is {num_1 / num_2}")
elif operator == "**":
    print(f"the value is {num_1 ** num_2}")

else:
    print("give me a operator to continue")

