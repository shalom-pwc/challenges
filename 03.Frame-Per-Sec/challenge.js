
//Frames Per Second
function  frames ( minutes , fps ) {

  const  fpsRes  =  fps  *  60 ;
  return  minutes  *  fpsRes ;
  
}
console.log(frames(1, 1));