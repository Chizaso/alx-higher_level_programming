#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let lastIndex = 0;
  let len = 0;
  while (list[len]) {
    len++;
  }
  lastIndex = len - 1;
  while (lastIndex >= 0) {
    newList.push(list[lastIndex]);
    lastIndex--;
  }
  return newList;
};
