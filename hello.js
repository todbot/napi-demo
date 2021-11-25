
   
//var addon = require('bindings')('hello');
var binding = require('node-gyp-build')(__dirname);

console.log(binding.hello()); // 'world'

