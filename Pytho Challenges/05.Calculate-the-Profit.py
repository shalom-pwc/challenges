# Calculate Profit
# ---------------------------------------
profite = {
   "costPrice": 55,
   "sellPrice": 65,
   "invontory": 1500
}
def totalProfite(profite):
  
      return (profite["sellPrice"] * profite["invontory"]) - (profite["costPrice"] * profite["invontory"])
  
  
print(totalProfite(profite))

# 150000