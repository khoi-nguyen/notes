# How to contribute

![Build](https://github.com/khoi-nguyen/teaching/workflows/Build/badge.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

## Setting up

- Install [Vagrant](https://vagrantup.com)
- Install [Virtualbox](https://www.virtualbox.org/)
- Install [Atom](https://atom.io/) with the following extensions
  (`Ctrl+comma` to open the settings, then go to the `+ Install` tab):
    - build (by noseglid)
    - pdf-view-plus (by Aerijo)
    - language-pfm (by leipert)
- Clone this repository in Atom (`Ctrl+Shift+8`, `Clone an existing Github repository`, Clone from `https://github.com/khoi-nguyen/teaching.git`)

Press `F7` and select `init`.

Open a `.md` file to edit, press `F7` and select current.
Subsequent builds can be triggered by pressing `F9`.

### For advanced users who don't want to use Atom

Run `$ docker run -v $(pwd):/teaching bknguyen/teaching all` from the project's directory to build everything.

## Additional steps if you want to contribute

- Create a [Github](https://github.com) account
- Log in on Github in Atom (`Ctrl+Shift+8`)
