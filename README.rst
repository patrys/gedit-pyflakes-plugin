:author: Anna Warzecha <anna.warzecha@gmail.com>, Gustavo Rezende <nsigustavo@gmail.com>

Gedit Pyflakes Plugin
======================

gedit-pyflakes-plugin allows users to run Pyflakes inside Gedit and show found pyflakes' error messages.


Download and install
===============

You can download gedit-pyflakes-plugin::

    $ wget -O gedit-pyflakes-plugin.tar.gz http://github.com/aniav/gedit-pyflakes-plugin/tarball/master
    $ tar -xzvf gedit-pyflakes-plugin.tar.gz

Put the geditpyflakes.plugin file and the whole content directory into ~/.local/share/gedit/plugins::

    $ cd aniav-gedit-pyflakes-plugin*
    $ mkdir ~/.local/share/gedit/plugins
    $ cp -rf * ~/.local/share/gedit/plugins

Install dependences: pynotify and pyflakes

In gedit main menu go to: Edit -> Preferences

In Preferences dialog go to Plugins tab.

Find 'Gedit Pyflakes Plugin' in plugin list and enable it. Done.



Getting involved!
==================

Gedit Pyflakes Plugins is in development state. It may be viewed and followed on github::

  http://github.com/aniav/gedit-pyflakes-plugin


Retrieve the source code using git::

    $ git clone git@github.com:aniav/gedit-pyflakes-plugin.git

