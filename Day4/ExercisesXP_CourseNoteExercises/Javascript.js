//Course note: Loop
//Exercise1

for (let i = 0; i <= 15; i++) {
//check if the number is even
if(i % 2 == 0) {
    console.log(i +" is even");
}

// if the number is odd
else {
    console.log(i +" is odd");
}
}


//Exercise 2
let NAMES= ["john", "sarah", 23, "Rudolf",34]
//if the item is not a string, pass.

/*for (let i = 0; i < NAMES.length;i++)
{
    String = typeof(NAMES[i]);
    if (String = "String") {
    console.log(NAMES[i])}
    else { break; }
   
} */

//1
for (let name of NAMES) {
    if (typeof (name) !== 'string') {
        continue;
    }
    let firstLetter = name.charAt(0)
    if ( firstLetter !== firstLetter.toUpperCase()) {
        name = firstLetter.toUpperCase() + name.slice(1);
    }
    console.log(name)
}

//2
for (let name of NAMES) {
    if (typeof (name) !== 'string') {
        continue;
    }
    console.log(name)
}



//Exercises XP
//Exercise 1 : List Of People

const people = ["Greg", "Mary", "Devon", "James"];

// Part I - Review About Arrays

//1
people.shift();
console.log(people)

//2
people[people.length - 1] = "Jason";
console.log(people)

//3
people.push("ben")
console.log(people)

//4
console.log(people.indexOf("Mary"))

//5
const PeopleCopy = people.slice(1)
console.log("PeopleCopy: ", PeopleCopy)

//6
console.log(people.indexOf("Foo"))
//Foo not present in Array People

//7
const last = people[people.length - 1]
console.log("last: ", last)

//Part II - Loops

//1
for (const person of people) { console.log("This person is: ", person)}

//2
for (const person of people) { 
    console.log("This person is: ", person)
    if (person === "Jason") {break}
}



//Exercise 2 : Your Favorite Colors

//1
const colors = ["black", "blue", "rosegold", "green", "red"]

//2
for (let i = 0; i < colors.length;i++)
{console.log("My #" + (i+1) + " choice is " + (colors[i]))}

//3
const suffixes = ["st", "nd","rd", "th", "th"]
for (let i = 0; i < colors.length;i++)
{console.log("My " + (i+1) + (suffixes[i])+ " choice is " + (colors[i]))}


//Exercise 3 : Repeat The Question

//1
let number = prompt("Enter number")
console.log("Number:", number)
type = typeof(number)
console.log(type)


//2
//convert type into number

while (number!=10) {
    let reply = prompt("Enter number")
    number = Number(reply)
}

//Exercise 4 : Building Management

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

//2
console.log(building.numberOfFloors)

//3
console.log("Number of apartments on 1st floor:", building.numberOfAptByFloor.firstFloor)
console.log("Number of apartments on 3rd floor:", building.numberOfAptByFloor.thirdFloor)

//4
SecondTenant = building.nameOfTenants[1]
console.log("second tenant: " + SecondTenant)
console.log(SecondTenant + " has " + (building.numberOfRoomsAndRent.dan[0]) + " rooms in his apartment")

//5
//Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
let SarahRent = building.numberOfRoomsAndRent.sarah[1]
console.log(SarahRent)
let davidRent = building.numberOfRoomsAndRent.david[1]
console.log(davidRent)
let danRent = building.numberOfRoomsAndRent.dan[1]
console.log(danRent)

davidAndsarahRent = SarahRent + davidRent
console.log(davidAndsarahRent)

if (davidAndsarahRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200
}
console.log(building)


//Exercise 5 : Family
let family = {Mum: "Nazimah", Dad: "Asraf", Brother: "Nafees"}

for (let key in family) {
    console.log("Key:", key)
    console.log("Value:", family[key])
}

//Exercise 6 : Rudolf
//Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

let phrase = " "
for (const key in details) {
phrase = phrase + " " + key +" " + details[key]
console.log(phrase)
}


//Exercise 7 : Secret Group
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let AlphabeticalOrder = names.sort() 
let letter = ""

for (const key of AlphabeticalOrder) { 
    console.log(key)
    letter = letter + key[0]
}
console.log(letter)


