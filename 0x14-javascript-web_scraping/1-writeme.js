#!/usr/bin/node
/* write a string to a file */
const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filePath, string, { encoding: 'utf-8', flag: 'w' }, (err) => {
  if (err) {
    console.log(err);
  }
});
