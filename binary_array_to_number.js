// #codewars.com 
// #problem 18
// #bekmuxtorov
// #binary_array_to_number  
// #Given an array of ones and zeroes, convert the equivalent binary value to an integer.
// JAVASCRIPT

function binary_array_to_number(array){
    let s = 0
    for(let i of array){
        s = s * 2 + i;
    }
    return s
}

const array = [0,0,0,1]
console.log(binary_array_to_number(array))

