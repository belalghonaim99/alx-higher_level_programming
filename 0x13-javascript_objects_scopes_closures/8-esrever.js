#!/usr/bin/node
/*
Write a function that returns the reversed version of a list:
Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
*/
exports.esrever = function (list) {
    return list.reduceRight(function (version, current_list) {
      version.push(current_list);
      return version;
    }, []);
  };