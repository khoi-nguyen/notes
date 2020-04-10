# How to contribute

![Build](https://github.com/khoi-nguyen/teaching/workflows/Build/badge.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

## Setting up

- Install [Docker](https://docker.com)
  - Widows:
    - [Windows 10 Enterprise](https://download.docker.com/win/stable/Docker%20Desktop%20Installer.exe)
    - [Other versions](https://github.com/docker/toolbox/releases/download/v19.03.1/DockerToolbox-19.03.1.exe)
  - MacOS:
    - [10.13 or newer, with hardware 2010 or newer](https://download.docker.com/mac/stable/Docker.dmg)
    - [Other versions](https://github.com/docker/toolbox/releases/download/v19.03.1/DockerToolbox-19.03.1.pkg)
  - Linux: use your package manager
- Install [Atom](https://atom.io/) with the following extensions
  (`Ctrl+comma` to open the settings, then go to the `+ Install` tab):
    - build (by noseglid)
    - pdf-view-plus (by Aerijo)
    - language-pfm (by leipert)
- Clone this repository in Atom (`Ctrl+Shift+8`, `Clone an existing Github repository`, Clone from `https://github.com/khoi-nguyen/teaching.git`)

To build the file you are working on, press `F9`.

### For advanced users who don't want to use Atom

Run `$ docker run -v $(pwd):/teaching bknguyen/teaching all` from the project's directory to build everything.

## Additional steps if you want to contribute

- Create a [Github](https://github.com) account
- Log in on Github in Atom (`Ctrl+Shift+8`)
