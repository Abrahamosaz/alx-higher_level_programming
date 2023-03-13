#!/usr/bin/node

const addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number.toString());
};

module.exports = { addMeMaybe };
