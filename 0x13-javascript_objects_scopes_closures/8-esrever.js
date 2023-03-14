#!/usr/bin/node

module.exports.esrever = function (list) {
  const newList = [];
  for (let x = list.length - 1; x >= 0; x--) {
    newList.push(list[x]);
  }
  return (newList);
};
