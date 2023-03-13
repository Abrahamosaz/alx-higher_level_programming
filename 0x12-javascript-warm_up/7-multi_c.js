#!/usr/bin/node

const firstArg = Number(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < firstArg; x++) {
    console.log('C is fun');
  }
}
