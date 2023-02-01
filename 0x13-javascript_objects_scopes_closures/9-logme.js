#!/usr/bin/node

let numberArgument = 0;

module.exports.logMe = function (item) {
  console.log(`${numberArgument}: ${item}`);
  numberArgument++;
};
