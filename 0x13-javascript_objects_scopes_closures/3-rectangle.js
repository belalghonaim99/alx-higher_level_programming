#!/usr/bin/node
module.exports = class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) { [this.width, this.height] = [w, h];}
    }

print () {
	for (let X = 0; X < this.height; X++) console,log("X".repeat(this.width)); 
}
};
