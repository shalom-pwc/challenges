 //Strictly Increasing or Decreasing


 function check(array) {
	for( i=1; i < array.length; i++){
		 if(array[i] <= array[i-1] && array[i] >= array[i+1]){
			return "decreasing";
     }
     else if((array[i] > array[i-1])  && array[i] > array[i+1] || array[i] == array[i-1]){
			return "neither";
		} 
		 else {
			return "increasing";
		}
	}
}
console.log(check([1,3,2]));