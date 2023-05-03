#!/usr/bin/node

const fsPromise = require('fs').promises;

async function readWriteFile (readPathA, readPathB, writePath) {
  try {
    const file1 = await fsPromise.open('./' + readPathA, 'r');
    const file2 = await fsPromise.open('./' + readPathB, 'r');
    const dataA = await file1.readFile('utf-8');
    const dataB = await file2.readFile('utf-8');
    const newData = dataA + dataB;
    const file3 = await fsPromise.open('./' + writePath, 'w');
    await file3.writeFile(newData, 'utf-8');
  } catch (err) {
    console.log(err);
  }
}
readWriteFile(process.argv[2], process.argv[3], process.argv[4]);
