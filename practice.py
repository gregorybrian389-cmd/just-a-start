operator=input("Enter your operator of choice (+, -, /, *):")
Numb1=float(input("Enter a number:"))
Numb2=float(input("Enter a second number"))
if operator == "+":
    result= Numb1 + Numb2
elif operator == "-":
    result = Numb1 - Numb2  
elif operator == "/":
    result = Numb1 / Numb2
elif operator == "*":
    result = Numb1 * Numb2
else:
    print(f"{operator} is not valid")     
print(result)
