#!/usr/bin/node
/*
Write a script that searches the second bigger
You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
*/

if (process.argv.length <= 3) {
    console.log(0);
} else {
    const list = process.argv.slice(2).map(Number);
    console.log(list.sort((a, b) => b - a)[1]);
}