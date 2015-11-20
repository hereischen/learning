'use strict';

var s = 'Hello';

function greet(name) {
	console.log(s + ',' + name + '!');
}

function shit(name) {
	console.log('shit ' + name)
}
module.exports = {
	shit : shit,
	greet : greet
}

// exports.shit = function (name) {
// 	console.log(s + ',' + name + '!');
// }