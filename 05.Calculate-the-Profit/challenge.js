
//Calculate the Profit

let profite = {
   costPrice: 55,
   sellPrice: 65,
   invontory: 1500
};
function totalProfite(profite){
  
      return (profite.sellPrice * profite.invontory) - (profite.costPrice * profite.invontory);
  }
  
  console.log(totalProfite(profite));

