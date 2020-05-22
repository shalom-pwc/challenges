# Strictly-Increasing-or-Decreasing
# -------------------------------------------------------------
def incre_decr(a, b, c):
  if(a < b) and (b < c):
    return "increasing"
  elif(a > b) and (b > c):
    return "decreasing"
  else:
    return "nither"

print(incre_decr(1,2,3))

# i = 0
# def check(array):
# 	for i in i <= len(array):
#     i += 1
#     if(array[i] <= array[i-1] & array[i] >= array[i+1]):
#     return "decreasing"
    
#     elif((array[i] > array[i-1])  & array[i] > array[i+1] | array[i] == array[i-1]):
#     return "neither"
  
#     else:
#     return "increasing"
	
# print(check([1,3,2]))