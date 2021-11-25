# napi-demo

Demonstration NAPI and prebuildify

Demo taken from https://github.com/nodejs/node-addon-examples/

The `helloworld.c` is not part of this demo, but added to show
simple Universal (fat) binary compilation and linking.


## Multi- arch test setup

```sh
# our current arch, M1 Mac
$ arch
arm64

# install arm version of node
$ nvm install 17.1.0

# install x86 version of node 
$ arch -x86_64 /bin/bash -c "source $HOME/.nvm/nvm.sh; nvm install v17.0.1"

# Change back to arm ndoe
$ nvm use 17.1.0

# Install our project, verify it works
$ npm install
$ npm run test

# Mdke prebuilds, remove temp build dir
$ npm run prebuild-darwin
$ rm -rf build

# Try out suppposed arm64 prebuild
$ npm run test
Error: dlopen(
[...]
(mach-o file, but is an incompatible architecture (have 'x86_64', need 'arm64e')), '/usr/local/lib/node.napi.node' (no such file), '/usr/lib/node.napi.node' (no such file)
    at Object.Module._extensions..node (node:internal/modules/cjs/loader:1179:18)
    at Module.load (node:internal/modules/cjs/loader:975:32)
    at Function.Module._load (node:internal/modules/cjs/loader:822:12)
    at Module.require (node:internal/modules/cjs/loader:999:19)
    at require (node:internal/modules/cjs/helpers:102:18)
    at load (/Users/tod/projects/node/napi-demo/node_modules/node-gyp-build/index.js:21:10)
    at Object.<anonymous> (/Users/tod/projects/node/napi-demo/hello.js:4:40)
    at Module._compile (node:internal/modules/cjs/loader:1097:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1149:10)
    at Module.load (node:internal/modules/cjs/loader:975:32) {
  code: 'ERR_DLOPEN_FAILED'
}

# Try out x86_64 node
nvm use v17.0.1
npm run test

# the above succeeeds
```


