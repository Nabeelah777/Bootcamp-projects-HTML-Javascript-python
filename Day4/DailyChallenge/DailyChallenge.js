//Daily Challenge: Stars
//1

let maxLine = 6
let stars = ""
for (let i = 0; i < maxLine ; i++) {
    stars = stars + " * "
    console.log(stars)
}

//2

for (let i = 0; i < maxLine; i++) {
    let StarNumber = i + 1
    let StarLine = ""

    for (let j = 0; j < StarNumber; j++) {
        StarLine = StarLine + " * "
    }
console.log(StarLine)
}