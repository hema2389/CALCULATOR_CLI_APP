while True:
  try:
    op=input("Enter the operation(add/sub/div/mul/percent/exit)").lower()
    if op=="exit":
      break
    a=float(input("Enter the first number:"))
    b=float(input("Enter the second number:"))
    if op=="add":
        print("The sum is:", a+b)
    elif op=="sub":
        print("The difference is:", a-b)
    elif op=="div":
      if b==0:
        print("Division cannot be done with 0")
      else:
        print("The quotient is:", a/b)
    elif op=="mul":
        print("The product is:", a*b)
    elif op=="percent":
      if b==0:
        print("Percentage cannot be calculated with divisor 0")
      else:
        print("The percentage is:", (a/b)*100,"%")
    else:
      print("Invalid operation")
  except ValueError:
    print("Invalid input. Enter numerical values only")
