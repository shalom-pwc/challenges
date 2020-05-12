//Is the Word Singular or Plural?
function isPlural(word) {
   let character = word.endsWith("s");

if (character=="s"){

console.log("Plural");

}
else{

console.log("singular");

}
}
    
isPlural('change');
    