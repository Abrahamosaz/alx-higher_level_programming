#!/usr/bin/node

const firstArg = Number(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < firstArg; x++) {
    console.log('X'.repeat(firstArg));
  }
}
