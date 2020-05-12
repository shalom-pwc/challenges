//Is the Number Even or Odd?
function oddOrEven(num1, num2){
  let num3 = num1 % num2;

      if (num3==0){

        return "Its Even number! ";

      }
      else{ 

        return "Its Odd number! ";

      }
}
    
console.log(oddOrEven(5,7));
