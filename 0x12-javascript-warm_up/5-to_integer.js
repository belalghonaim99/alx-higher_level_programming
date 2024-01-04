#!/usr/bin/node
/*
script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

If the argument can’t be converted to an integer, print “Not a number”
You must use console.log(...) to print all output
You are not allowed to use var
*/
const number = parseInt(process.argv[2]);

if (!isNaN(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
