#!/usr/bin/node

const arg = process.argv[2];
if (isNaN(parseInt(arg))) {
  console.log('Missing number of occurrences');
} else {
  const argInt = parseInt(arg);
  let i;
  for (i = 0; i < argInt; i++) {
    console.log('C is fun');
  }
}
