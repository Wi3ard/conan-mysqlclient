[ ![Download](https://api.bintray.com/packages/bincrafters/public-conan/mysql-connector-c%3Abincrafters/images/download.svg) ](https://bintray.com/bincrafters/public-conan/mysql-connector-c%3Abincrafters/_latestVersion)
[![Build Status](https://api.travis-ci.org/Wi3ard/mysql-connector-c.svg?branch=release%2F6.1.11)](https://travis-ci.org/Wi3ard/mysql-connector-c)
[![Build status](https://ci.appveyor.com/api/projects/status/wxnsuv71wxx86wgk?svg=true)](https://ci.appveyor.com/project/Wi3ard/conan-mysqlclient)

---

**This repository moved. Please use the new [location](https://github.com/bincrafters/conan-mysql-connector-c)**

---

[Conan.io](https://conan.io) package for [MySQL Connector/C](https://dev.mysql.com/downloads/connector/c/) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/mysql-connector-c%3Abincrafters).

## For Users: Use this package

### Basic setup

    $ conan install mysql-connector-c/6.1.11@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    mysql-connector-c/6.1.11@bincrafters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires", and then running the build() method.

    $ conan create bincrafters/stable

## Add Remote

    $ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload mysql-connector-c/6.1.11@bincrafters/stable --all -r bincrafters

## License
[GPLv2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
