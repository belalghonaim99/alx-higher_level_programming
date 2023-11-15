#!/usr/bin/node
/*
Write a class Rectangle that defines a rectangle:
You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
*/
module.exports = class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
    }
  
    rotate () {
      [this.width, this.height] = [this.height, this.width];
    }
  
    double () {
      [this.width, this.height] = [this.width * 2, this.height * 2];
    }
  };