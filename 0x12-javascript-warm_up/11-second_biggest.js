#!/usr/bin/node

let [, , ...numberArray] = process.argv;
numberArray = numberArray.map((value) => Number(value));

if (numberArray.length <= 1) {
  console.log(0);
} else {
  numberArray.sort();
  console.log(numberArray[numberArray.length - 2]);
}
