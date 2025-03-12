def add (x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def division(x,y):
  if y!=0:
    return x/y
def modulus(x,y):
  if y!=0:
    return x%y
  else:
    return "Error! division by zero."
def calculator():
  print("Simple calculator")
  print("Choose calculator")
  print("1. ADD")
  print("2. SUBTRACT")
  print("3. MULTIPLY")
  print("4. DIVIDE")
  print("5. MODULUS")

  while True:
    choice = input("Enter choice (1/2/3/4/5):")

    if choice in ['1','2','3','4','5']:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

      if choice == '1':
        print(f"the result is : {add(num1,num2)}")
      elif choice == '2':
        print(f"the result is : {subtract(num1,num2)}")
      elif choice == '3':
        print(f"the result is : {multiply(num1,num2)}")
      elif choice == '4':
        print(f"the result is : {divide(num1,num2)}")
      elif choice == '5':
        print(f"the result is : {modulus(num1,num2)}")


      next_calculation = input("DO you want perform another calculation? (yes/no):")
      if next_calculation.lower() != 'yes':
        break
      
    else:
      print("Invalid input")
calculator()
