#!/usr/bin/node

const dict = require('./101-data.js').dict;
const dictValues = Object.values(dict);
const set = new Set(dictValues);
const newDict = {};
let dictItem = '';

for (const item in dict) {
  if (set.has(dict[item])) {
    dictItem = dict[item].toString();
    if (newDict[dictItem] === undefined) {
      newDict[dictItem] = [item];
    } else {
      newDict[dictItem].push(item);
    }
  }
}
console.log(newDict);
