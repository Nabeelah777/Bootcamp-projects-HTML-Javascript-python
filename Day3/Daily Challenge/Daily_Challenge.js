let sentence = "The movie is not that bad, I like it"

let wordNot = sentence.indexOf("not");

let wordBad = sentence.indexOf("bad");

console.log(wordNot); //position of not
console.log(wordBad); //position of bad

if (wordNot === -1) { console.log(sentence)}
else if (wordNot < wordBad)
{ let first = sentence.slice(0, wordNot)
let second = sentence.slice(wordBad + 3)
console.log(first + "good" + second) }

else { console.log(sentence)}



