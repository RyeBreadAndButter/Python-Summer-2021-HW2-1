def number_converter(base):
  if 2 <= base and base <= 16:
    print("valid number")

  else:
    print('invalid number')



x = int(input("Welcome to the base converter. Please enter inital base and numbers to convert"))

number_converter(x)