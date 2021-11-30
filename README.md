
# Odoo App DebugPY for Visual Studio Code


## Description

This module enable debugpy on Odoo. 

With debugpy and Visual Studio Code you can see what Python is doing during the process, you can stop it (breakpoint) or/and check variables, call stacks and more. 

The purpose is to be used on develop and test environments.

## Installation

```bash
pip install debugpy
```
On odoo Application App search for debugpy and install it

## Visual Studio Code

Create or configure launch.json file.

Open CTRL or CMD + SHIFT + D

If launch.json is already present, on top the left section, to the icon Gear open the related file. Otherwise you will see a button for create the json file.

insert this code, be sure to change IP Address!

```json
{
 	"version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Debugpy",
            "type": "python",
            "request": "attach",
            "port": 5678,
            "host": "10.0.0.1",
        }
    ]
}

```

## Run the debugger

On the code you are looking for, put a breakpoint (near codeline numbers on the left), then press F5 to start debugger. Load the Odoo page, corresponding where your code belongs a wait process stop on the breakpoint.

## Changelog

- Initial version