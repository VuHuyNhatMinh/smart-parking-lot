Parking_management
==================

This is a Web server parkingmanagement, It's build by Node-red on Node.js, taking full advantage of its event-driven, non-blocking model. This makes it ideal to run at the edge of the network on low-cost hardware such as the Raspberry Pi as well as in the cloud.

Installing with npm
To install Node-RED you can use the npm command that comes with node.js:

sudo npm install -g --unsafe-perm node-red
If you are using Windows, do not start the command with sudo.

That command will install Node-RED as a global module along with its dependencies.

You can confirm it has succeeded if the end of the command output looks similar to:

+ node-red@1.1.0
added 332 packages from 341 contributors in 18.494s
found 0 vulnerabilities
Installing with docker
To run in Docker in its simplest form just run:

docker run -it -p 1880:1880 --name mynodered nodered/node-red

Running
Once installed as a global module you can use the node-red command to start Node-RED in your terminal. You can use Ctrl-C or close the terminal window to stop Node-RED.

$ node-red

You can then access the Node-RED editor by pointing your browser at http://localhost:1880.

The log output provides you various pieces of information:

The versions of Node-RED and Node.js
Any errors hit when it tried to load the palette nodes
The location of your Settings file and User Directory
The name of the flows file it is using.
Node-RED uses flows_<hostname>.json as the default flows file. You can change this by providing the flow file name as argument to the node-red command.

import this project file : flow.json
- click import from menu --> select import a file to import (flow.json) --> import

Deploy project and UI web  : http://localhost:1880/ui

### About

This is your project's README.md file. It helps users understand what your
project does, how to use it and anything else they may need to know.
