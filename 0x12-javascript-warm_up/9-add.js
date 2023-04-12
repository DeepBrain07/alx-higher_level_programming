#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}
const argInt1 = parseInt(process.argv[2]);
const argInt2 = parseInt(process.argv[3]);
add(argInt1, argInt2);
