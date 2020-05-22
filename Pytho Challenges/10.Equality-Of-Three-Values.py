# Equality-Of-Three-Values
# --------------------------------------------------
def equal(num1, num2, num3):
  if((num1 == num2) and (num1 == num3)):
    return "Three are equal"
  elif((num1 == num2) or (num1 == num3) or (num2 == num3)):
    return "Two are equal"
  else:
    return "Not equal"

print(equal(7,7,7))

# Three are equal