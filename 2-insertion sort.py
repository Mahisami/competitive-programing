'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

function insertionSort1(n, arr) {
    // Write your code here

 const lastNum = arr[n - 1]
 
 for (let index = n - 2; index >= 0; index--){
      let current = arr[index]
      if (current > lastNum) {
            arr.splice(arr.indexOf(current)+1, 1, current)
            console.log(arr.join(' '))
      } 
      else if (current < lastNum){
            arr.splice(arr.indexOf(current)+1, 1, lastNum)
            console.log(arr.join(' '))
            break;
      }
 }
}


function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    insertionSort1(n, arr);
}
