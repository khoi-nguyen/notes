# How to contribute

![Build](https://github.com/khoi-nguyen/teaching/workflows/Build/badge.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)

## Setting up

### OS/X and Windows

- Install [Vagrant](https://vagrantup.com)
- Install [Virtualbox](https://www.virtualbox.org/)
- Install [Atom](https://atom.io/) with the following extensions
  (`Ctrl+comma` to open the settings, then go to the `+ Install` tab):
    - build (by noseglid)
    - pdf-view-plus (by Aerijo)
    - language-pfm (by leipert)
- Clone this repository in Atom (`Ctrl+Shift+8`, `Clone an existing Github repository`, Clone from `https://github.com/khoi-nguyen/teaching.git`)

Press `F7` and select `start_vm`.
This could take a while depending on your internet connection.

Open a `.md` file to edit (e.g. `12/differentiation.md`),
press `F7` and select `current`.
After the build, you can open the generated PDF (e.g. `12/differentiation.handout.pdf`).
Subsequent builds can be triggered by pressing `F9`,
which repeats the last build (`F7`).

### Linux

- Install `docker` and `docker-compose`
- Clone the directory
- Run `docker-compose run make`

## Additional steps if you want to contribute

- Create a [Github](https://github.com) account
- Log in on Github in Atom (`Ctrl+Shift+8`)
