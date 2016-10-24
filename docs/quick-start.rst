Quick Start Guide
=================

Simple steps to get started.

Clone and initialize
--------------------

Here are the steps::

  $ cd /usr/dev
  $ git clone https://github.com/leocornus/leocornus.buildout.boilerplate.git boilerplate
  $ cd boilerplate
  $ git submodule init
  $ git submodule update

Update base folder and buildout
-------------------------------

We need edit the **buildout-local.cfg** to update 
the **base-folder** variable.
Here are the commands:: 

  $ cd /usr/dev/boilerplate
  $ python bootstrap.py
  $ bin/buildout -N -c buildout-init.cfg
  $ bin/buildout -N

Tweak local settings
--------------------

Local settings including the following items:

* ports, hosts, ips, users, etc.
* application configurations
