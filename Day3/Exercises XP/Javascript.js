//class Notes :Conditionals
//Exercise 1

//let age = prompt("Please enter your age");
//if (age < 18) { alert ('Sorry, you are too young to drive this car. Powering off')}
   // else if (age === 18){ alert ("Congratulations on your first year of driving. Enjoy the ride!")} 
   // else { alert ("Powering On. Enjoy the ride!")}


//class Notes :Introduction On Objects
//Exercise 1





//Exercises XP
//Exercise 1: Simple If/Else Statement

let x = 5;
let y = 2;

if (x>y) { console.log("x is the biggest number")}

else {console.log("y is the biggest number")}


//Exercise 2: Chihuahua
let newDog = "Chihuahua";
let length = newDog.length;
console.log(length)
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())
switch(newDog) {
    case 'Chihuahua':
        console.log("I love Chihuahuas, it's my favorite dog breed");
        break;
    default:
        console.log("I don't care, I prefer cats");
}

//Exercise 3: Even Or Odd

const number = prompt("Enter a number: ");

//check if the number is even
if(number % 2 == 0) {
    console.log(number +" is an even number");
}

// if the number is odd
else {
    console.log(number +" is an odd number");
}


//Exercise 4: Group Chat

const users = ["Lea123", "Princess45" , "cat&doglovers", "helooo@000"];
onlineUser = users.length
if (onlineUser === 0) {console.log("no one is online")}

if (onlineUser === 1) {console.log(users[0] + " is online")}

if (onlineUser === 2) {console.log(users[0] + " and " + users[1] + " are online")}

if(onlineUser > 2) {console.log(users[0] + ", " + users[1] + " and " + (onlineUser - 2) + " more are online")}

