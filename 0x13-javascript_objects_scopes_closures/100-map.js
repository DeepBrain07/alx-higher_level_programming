#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((x) => {
  const index = list.indexOf(x);
  if (index === 0) {
    x *= 0;
    return (x);
  } else {
    x = x * list[index - 1];
    return (x);
  }
});
console.log(list);
console.log(newList);
