def adder(value1, value2):
   return value1 + value2

def subtract(value1, value2):
   return value1 - value2

def multiply(value1, value2):
   return value1 * value2

def divide(value1, value2):
   return value1 / value2

print("Welcome to myCalculation")
print("--------------------------")
print("Please Enter Your First Value")
value1 = int(input("First Value: "))
print("Please Enter Your Second Value")
value2 = int(input("Second Value: "))


print("Choose an operator for results of Sum")
print("1.+(Adder)")
print("2.-(Subtract)")
print("3.*(Multiply)")
print("4./(Divide)")
optr = (input("Choice Operator:"))
val_1 = value1;
val_2 = value2;

#Adder
if optr == '+':
   print(val_1, "+",val_2, "=", adder(val_1,val_2))
elif optr == '1':
    print(val_1, "+",val_2, "=", adder(val_1,val_2))
elif optr == 'Adder':
    print(val_1, "+",val_2, "=", adder(val_1,val_2))
elif optr == 'adder':
    print(val_1, "+",val_2, "=", adder(val_1,val_2))

#Subtract
elif optr == '-':
   print(val_1, "-", val_2, "=", subtract(val_1,val_2))
elif optr == '2':
   print(val_1, "-", val_2, "=", subtract(val_1,val_2))
elif optr == 'Subtract':
   print(val_1, "-", val_2, "=", subtract(val_1,val_2))
elif optr == 'subtract':
   print(val_1, "-", val_2, "=", subtract(val_1,val_2))

#Multiply
elif optr == '*':
   print(val_1, "*",val_2, "=", multiply(val_1,val_2))
elif optr == '3':
   print(val_1, "*",val_2, "=", multiply(val_1,val_2))
elif optr == 'Multiply':
   print(val_1, "*",val_2, "=", multiply(val_1,val_2))
elif optr == 'multiply':
   print(val_1, "*",val_2, "=", multiply(val_1,val_2))

#Divide
elif optr == '/':
   print(val_1, "/",val_2, "=", divide(val_1,val_2))
elif optr == '4':
   print(val_1, "/",val_2, "=", divide(val_1,val_2))
elif optr == 'Divide':
   print(val_1, "/",val_2, "=", divide(val_1,val_2))
elif optr == 'divide':
   print(val_1, "/",val_2, "=", divide(val_1,val_2))

else:
   print("Please Enter Operator")

