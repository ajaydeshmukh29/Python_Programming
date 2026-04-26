# num = int(input("What's X? "))
# print(f"X is {num}")

#with exception
#


#NameError
# try:
#   n = int(input("What's x? "))
# except ValueError:
#   print("X is not an integer")

# print(f"x is {x}")

#else 
try:
  x = int(input("whats is x? "))
except ValueError:
  print("X is not an enteger")
else:
  print(f"x is {x}")