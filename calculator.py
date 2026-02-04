def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return 0
    else:
        return x/y
operators={"add":add,
           "subtract":subtract,
            "multiply":multiply,
           "divide":divide}
def main():

    print("options:\n1)add\n2)sub\n3)mul\n4)div")
    user_input = input("Enter a option:")
    if user_input in operators:
        x=float(input("Enter a number:"))
        y=float(input("Enter another number:"))
        result = operators[user_input](y,x)
        print("Answer:", result)
    else:
        print("Invalid option")
main()
