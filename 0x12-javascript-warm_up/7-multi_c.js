#!/usr/bin/node
/*
write a script that prints x times “C is fun”
Where x is the first argument of the script
If the first argument
*/

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
