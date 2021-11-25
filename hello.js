

var binding1 = require('node-gyp-build')(__dirname);  // just hello1.node
var binding2 = require('node-gyp-build')(__dirname);  // just hello2.node

console.log(binding1.hello1()); // 'hello1world'
console.log(binding2.hello2()); // 'hello2world'
