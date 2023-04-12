#!/usr/bin/node

const args = process.argv;
let max = 0;
for (let i = 2; i < args.length; i++) {
  const temp = parseInt(args[i]);
  if (temp >= max) {
    max = temp;
  }
}
let max2 = 0;
for (let j = 2; j < args.length; j++) {
  const temp2 = parseInt(args[j]);
  if (temp2 !== max && temp2 >= max2) {
    max2 = temp2;
  }
}
console.log(max2);
