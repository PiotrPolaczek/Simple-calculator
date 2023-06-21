a = None
b = None
c = None

a = input("Enter a: ")
b = input("Enter b: ")
c = input("What action do you want to perform? Addition, subtraction, multiplication, division")

if c == "addition":
    print(int(a) + int(b))
elif c == "subtraction":
    print(int(a) - int(b))
elif c == "multiplication":
    print(int(a) * int(b))
elif c == "division":
    print(int(a) / int(b))
else:
    print("Invalid action")