#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, { encoding: 'utf-8', flag: 'r' }, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
