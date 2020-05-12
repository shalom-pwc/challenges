// Extract City Facts
let city = {
  name: "Asmara",
  population: "1,000,000",
  continent: "Africa"
};

function cityFacts(city) {
  let name = city.name; 
  let population = city.population;
  let continent = city.continent;
  return name + ' has a population of ' + population + ' and is situated in ' + continent;
}
 console.log(cityFacts(city));