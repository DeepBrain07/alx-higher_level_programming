#!/usr/bin/node

const arg = process.argv[2];
if (isNaN(parseInt(arg))) {
  console.log('Missing size');
} else {
  const argInt = parseInt(arg);
  let i;
  let j;
  for (i = 0; i < argInt; i++) {
    let square = '';
    for (j = 0; j < argInt; j++) {
      square = square + 'X';
    }
    console.log(square);
  }
}
