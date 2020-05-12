//Count genders
let countGender = [
  {
    name: 'selam',
    gender: 'FEMAL'
  },
  {
    name: 'Dani',
    gender: 'MALE'
  },
  {
    name: 'Eva',
    gender: 'FEMAL'
  },
  {
    name: 'Sami',
    gender: 'MALE'
  },
  {
    name: 'Abel',
    gender: 'MALE'
  },
  {
    name: 'Fiori',
    gender: 'FEMAL'
  },
];

let Boys = 0;
let Girls = 0;


countGender.forEach(function(person){
  if(person.gender === "MALE"){
    Boys++;
  }
  else {
    Girls++;
  }
});

console.log(" My list contains " + Boys + " boys and " + Girls + " girls " );