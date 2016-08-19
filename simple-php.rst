Simple PHP application package
==============================

We will get stared with the simple PHP application package case.
The PHP package will target at the basic requirement for hosting
the MediaWiki site.
Here are the minimum requirement:

- MariaDB as the database server
- PHP and PHP-FPM
- Nginx as the Web server
- Parsoid (Node.js) service
- Elasticsearch for the search engine
- Supervisord as the process manager

.. contents:: Table of contents
   :depth: 5

Overview
--------

folder structure

How buildout config files are organized?

Buildout will use the last occurrence of this variable to overwrite
all previous occurrences.
In this case here, settings in file **buildout-local.cfg** 
will be the last occurrence.

Strategy for configruation files
--------------------------------

Configuration files should be stored within the application.
It is reasonable to check the configuration file inside
the correspoding application.
By default generated configuration files are stored in folder::

  ${settings:etc-directory}

It is defined in file **config/base.cfg**, using 
**${buildout:directory}/etc** as the default value.
We will use the default value here for all applications.
So application config files will be stored in the **etc** folder
of the application itself.
For example:

- Config files for MaridDB are in folder **mariadb/etc**
- Config files for PHP are in folder **php/etc**

Strategy for log files
----------------------

The buildout variable for log files is::

  ${settings:log-directory}

It is more convenient if we keep all log files in one location.
It is easier for analysing, debuging, and maintainence.
So in our case here, we will set the log folder to **sys/var/log**.
Here is the settings in file **buildout-local.cfg**::

  [settings]
  log-directory = {:sys-folder}/var/log

Strategy for Nginx vhost
------------------------

We will use virtual host for Nginx to server multiple applications.
This section will discuss the strategy to manage Nginx virtual host.

Step by step
------------

Here are the steps for how we build the PHP package:

#. clone the boilerplate, update submodule
#. check the dependences for MariaDB, PHP and Nginx,
#. edit the buildout-local.php to fit your local environment
#. bootstrap (python bootstrap.py) the project. boilerplate.
#. build MariaDB
#. build PHP and PHP-FPM, PHP depends on MariaDB
#. build Nginx web server
#. build the phpinfor app
#. build Nodejs and Parsoid
#. build Java and Elasticsearch server
#. build the wpmw app, WordPress and MediaWiki

Dependences list
''''''''''''''''

TODO: install dependences for different platform.

Local settings
''''''''''''''

Define your softwar stack here.
TODO: important local setting variables:

- base folder

Initialize buildout
'''''''''''''''''''

Bootstrap the buildout folder for each software.

Build
'''''

execute the buildout, build, install, and config

Build MariaDB

Here are the simple steps to build MariaDB::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-mariadb
  $ bin/buildout -N install build-mariadb


Build PHP-FPM

Here are the steps to build PHP-FPM::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-php
  $ bin/buildout -N install build-php

Build Nginx

Here are the steps to build PHP-FPM::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-nginx
  $ bin/buildout -N install build-nginx

Build sys (All in one)

using the include section for all in one superver config::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-sys
  $ bin/buildout -N install build-sys

Initilize server & data
'''''''''''''''''''''''

initialize MariaDB

The part **init-mariadb** will initialize the MariaDB server.::

  $ cd boilerplate/mariadb
  $ bin/buildout -N install init-mariadb

Start services
''''''''''''''

Applications
------------

A list of PHP applications for the boilerplate.

Simple PHP application phpinfo
''''''''''''''''''''''''''''''

The simple PHP application to show system information about
the software stack.

Questions
---------

- the strategy for configuration files
- the strategy for log files pid files
- the strategy for data folder
- How to generate the all in one supervisord.
  Using the **include** section
