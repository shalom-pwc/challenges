# Is-the-Word-Singular-or-Plural
# -----------------------------------------------
def is_singular(text):
   char = text[-1]
   if(char == "s") :
    return "Plular"
   else: 
    return "Singular"

print(is_singular("changes"))

# Plular