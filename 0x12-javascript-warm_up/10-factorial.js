#!/usr/bin/node

function factorial (arg) {
  if (isNaN(parseInt(arg)) || (arg === 1)) {
    return (1);
  }
  arg = parseInt(arg);
  return (arg * factorial(arg - 1));
}
console.log(factorial(process.argv[2]));
