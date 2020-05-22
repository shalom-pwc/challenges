# Strictly-Increasing-or-Decreasing
# -------------------------------------------------------------
def incre_decr(a, b, c):
  if(a < b) and (b < c):
    return "Increasing"
  elif(a > b) and (b > c):
    return "Decreasing"
  else:
    return "Neither"

print(incre_decr(1,2,3))

# Increasing