#!/usr/bin/node
/*
Write a script that prints a message depending of the number of arguments passed:

If no arguments are passed to the script, print “No argument”
If only one argument is passed to the script, print “Argument found”
Otherwise, print “Arguments found” */
if (process.argv.length === 0) {
    console.log('No argument');
} else if (process.argv.length === 1){
    console.log('Argument found');
} else {
    console.log('Argument found');
}