#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((x) => {
  const index = list.indexOf(x);
  x *= index;
  return (x);
});
console.log(list);
console.log(newList);
