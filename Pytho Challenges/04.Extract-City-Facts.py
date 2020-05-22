# EXTRACT CITY FACTS
#------------------------------------------------
city = {
  "name": "Asmara",
  "population": "1,000,000",
  "continent": "Africa"
}
def cityFacts(city):
   name = city["name"]
   population = city["population"]
   continent = city["continent"]
   return f"{name} has a population of  {population} and is situated in {continent}"

print(cityFacts(city))

# Asmara has a population of  1,000,000 and is situated in Africa