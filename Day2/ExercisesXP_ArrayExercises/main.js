//Introduction To JavaScript
//Exercise 1

let addressNumber, addressStreet, country;

addressNumber = "04";
addressStreet = "Royal Road Caroline";
country = "Mauritius";

let globalAddress = "I live at " + addressStreet + " " + addressNumber + ", " + "in " + country;
console.log(globalAddress)


//Exercise 2

let BirthYear, CurrentYear, Age;

BirthYear = "1996";
FuturYear = "2022";
Age = FuturYear - BirthYear;

let NewAge = "I will be " + Age + " in " + FuturYear;
console.log(NewAge)


//Javascript Arrays
//Exercise 3

let pets = ["cat", "dog", "fish", "rabbit", "cow"]; 
let dog = pets[1];
console.log(dog)

pets.unshift("horse")
console.log(pets)

pets.splice(4, 1); 
console.log(pets)
console.log(pets.length)


//Exercises XP
//Exercise 1 : Your Favorite Food

let FavoriteFood, FavoriteMeal;

FavoriteFood = "pizza";
FavoriteMeal = "dinner";
let FavMealDinner = "I eat " + FavoriteFood + " at every " + FavoriteMeal;
console.log(FavMealDinner)


//Exercise 2 : Series
//Part1

const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
console.log(myWatchedSeriesLength)


let series1 = myWatchedSeries.slice(0,2);
let series2 = myWatchedSeries.slice(-1);
let myWatchedSeriesSentence = series1 + " and " + series2;
console.log(myWatchedSeriesSentence)

let sentence = "I watched " + myWatchedSeriesLength + " series" + " : " + myWatchedSeriesSentence;
console.log(sentence)

//Part2

myWatchedSeries[2] = "friends"

myWatchedSeries.push("Vinchenzo"); 

myWatchedSeries.unshift("the king");

myWatchedSeries.splice(1, 1);

let thirdletter = myWatchedSeries[1][2];
console.log(thirdletter)

console.log(myWatchedSeries)

//Exercise 3 : The Temperature Converter

let celsius, fahrenheit;

celsius = 22;
fahrenheit = ((celsius/5)*9)+32;
let temperature = celsius + " ℃ " + "is " + fahrenheit + " ℉";
console.log(temperature)


//Exercise 4 : Guess The Answers #1

    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:55  (34+21)
    // Actual:55

    a = 2;

    console.log(a+b) //second expression
    // Prediction:23   (2+21)
    // Actual:23


//What will be the outcome of a + b in the first expression ?  55
//What will be the outcome of a + b in the second expression ? 23
//What is the value of c? undefined
//Analyse the code below, what will be the outcome? 75  (sum of (3+4) concatenate with 5

console.log(3 + 4 + '5');


//Exercise 5 : Guess The Answers #2

typeof(15)
// Prediction: number
// Actual:

typeof(5.5)
// Prediction:number
// Actual:

typeof(NaN)
// Prediction:number
// Actual:

typeof("hello")
// Prediction: string
// Actual:

typeof(true)
// Prediction:boolean
// Actual:

typeof(1 != 2)
// Prediction:boolean
// Actual:

"hamburger" + "s"
// Prediction: hamburgers
// Actual:

"hamburgers" - "s"
// Prediction: NaN
// Actual:

"1" + "3"
// Prediction: 13
// Actual:

"1" - "3"
// Prediction:NaN
// Actual:

"johnny" + 5
// Prediction: Johnny5
// Actual:

"johnny" - 5
// Prediction:NaN
// Actual:

99 * "hello"
// Prediction:NaN
// Actual:

1 != 1
// Prediction: false
// Actual:

1 == "1"
// Prediction:true
// Actual:

1 === "1"
// Prediction:false
// Actual:


//Exercise 6 : Guess The Answers #3

5 + "34"
// Prediction:534
// Actual:

5 - "4"
// Prediction:-4
// Actual:

10 % 5
// Prediction:0
// Actual:

5 % 10
// Prediction:5
// Actual:

"Java" + "Script"
// Prediction:JavaScript
// Actual:

" " + " "
// Prediction:  
// Actual:

" " + 0
// Prediction: 0
// Actual:

true + true
// Prediction: true
// Actual:2

true + false
// Prediction:1
// Actual:

false + true
// Prediction:1
// Actual:

false - true
// Prediction:-1
// Actual:

!true
// Prediction: false
// Actual:

3 - 4
// Prediction:-1
// Actual:

"Bob" - "bill"
// Prediction: NaN
// Actual: