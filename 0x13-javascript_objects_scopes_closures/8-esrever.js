#!/usr/bin/node

module.exports.esrever = function (list) {
  const reverseList = [];
  reverseRec(list, 0, reverseList);
  return (reverseList);
};

function reverseRec (list, index, reverseList) {
  if (index === list.length) {
    return;
  }
  reverseRec(list, index + 1, reverseList);
  reverseList[(list.length - 1) - index] = list[index];
}
