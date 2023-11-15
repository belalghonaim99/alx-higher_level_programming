#!/usr/bin/node
/*
Write a function that converts a number from base10

Prototype: exports.converter = function (base)
You are not allowed to import any file
You are not allowed to declare any new variable (var, let, etc..)
*/
exports.converter = function (base) { return base_number => base_number.toString(base); };