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

# install arm version of node, using 17.1.0
$ nvm install 17.1.0

# install x86_64 version of node, using 17.0.1
$ arch -x86_64 /bin/bash -c "source $HOME/.nvm/nvm.sh; nvm install 17.0.1"

# Change back to arm64 node
$ nvm use 17.1.0

# Install our project, verify it works
$ npm install
$ npm run test

# Make prebuilds and remove temp build dir
$ npm run prebuild-darwin
$ rm -rf build

# Try out arm64 prebuild
$ npm use 17.1.0
$ npm run test

# Try out x86_64 node, which succeeds
nvm use 17.0.1
npm run test

# Here's what the 'prebuilds' dir has:
$ ls -R prebuilds
darwin-x64+arm64/
prebuilds/darwin-x64+arm64:
node.napi.node*

$ file prebuilds/darwin-x64+arm64/node.napi.node
prebuilds/darwin-x64+arm64/node.napi.node: Mach-O 64-bit bundle x86_64

```


