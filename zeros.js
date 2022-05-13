// #codewars.com 
// #problem 20
// #bekmuxtorov
// #zeros
// #Write a program that will calculate the number of trailing zeros in a factorial of a given number.
// JavaScript

function zeros(n){
    let fives = 0;
    for (let i=5; i<=n; i *= 5){
        fives += parseInt(n / i)
    }

    return fives
}

let n=6
console.log(zeros(n))

