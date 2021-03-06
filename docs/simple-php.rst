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
''''''''''''''''''''''''''''''''

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
''''''''''''''''''''''

The buildout variable for log files is::

  ${settings:log-directory}

It is more convenient if we keep all log files in one location.
It is easier for analysing, debuging, and maintainence.
So in our case here, we will set the log folder to **sys/var/log**.
Here is the settings in file **buildout-local.cfg**::

  [settings]
  log-directory = {:sys-folder}/var/log

Log rotation strategy
'''''''''''''''''''''

The strategy for log rotation.
Mainly, we need worry about the Nginx server's log file,
especially the access log file.
We need rotate it every day!

Strategy for Nginx vhost
''''''''''''''''''''''''

We will use virtual host for Nginx to server multiple applications.
This section will discuss the strategy to manage Nginx virtual host.

Step by step
------------

Here are the steps for how we build the PHP package:

#. clone the boilerplate, update submodule
#. check the dependences for MariaDB, PHP and Nginx,
   (TODO: a buildout part to check dependences and install them)
#. edit the buildout-local.php to fit your local environment
#. bootstrap (python bootstrap.py) the project.
#. execute the initialization buildout parts, **buildout-init.cfg**.
   bin/buildout -N -c buildout-init.cfg
#. execute the buildout: **bin/buildout -N**
#. start all services by using supervisord.

Dependences list
''''''''''''''''

TODO: install dependences for different platform.

Local settings
''''''''''''''

Define your software stack here.
We have to use the absolute pathe for the important 
local setting variables **${settings:base-folder}**.
The file **buildout-local.cfg** will be symlinked to all
buildout components, including PHP, MariaDB, Nginx, etc.
The dependence between buildout components 
are tied with this variable.

For example, when we build PHP we need find MariaDB library.
The base-folder will be used to find the location for 
MariaDB binary files.

Initialize buildout
'''''''''''''''''''

Bootstrap the buildout folder for each software.::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg

Build
'''''

execute the buildout, build, install, and config
Here are the simple steps::

  $ cd boilerplate
  $ bin/buildout -N

Initilize server & data
'''''''''''''''''''''''

initialize MariaDB

The part **init-mariadb** will initialize the MariaDB server.::

  $ cd boilerplate/mariadb
  $ bin/buildout -N install init-mariadb

Start services
''''''''''''''

Using supervisord to start servvices::

  $ cd boilerplate
  $ sudo sys/bin/supervisord

Applications
------------

A list of PHP applications for the boilerplate.

Simple PHP application phpinfo
''''''''''''''''''''''''''''''

The simple PHP application to show system information about
the software stack.
Which includes phpinfo(), MariaDB information, etc.

As we use de-centralized strategy for buildout config files,
it is so easy to build this simple PHP application.
All we need is configuring a Ngnix virtual host server.
And then, let the Ngnix server load this virutal host server
(using the include directive).

Here are the steps to create the simple PHP application:

#. make the folder **app-phpinfo**
#. set up buildout-local.cfg and buildout-init.cfg for the new 
   phpinfo application.
#. execute buildout part init-app-phpinfo
#. Now we have a empty buildout.cfg file in folder **app-phpinfo**.
#. edit the **buildout.cfg** to set up buildout variables:
     - hosts:fronteend-ip
     - hosts:frontend-hostname
     - ports:nginx
     - settings:document-root
#. edit the **buildout.cfg** to customize the part
   **nginx-fpm-server** for the following variables:
     - error_log
     - access_log
     - fastcgi_pass
     - nginx-build-location
#. execute buildout, then will will have our first simple PHP
   application ready.

Here is the minimium **buildout.cfg** file::

  [buildout]
  extends =
      buildout-dev.cfg
      buildout-local.cfg
  
  parts =
      nginx-conf-server
      phpinfo-php
  
  [hosts]
  frontend-ip = 10.160.192.88
  frontend-hostname = ${:frontend-ip}
  
  [ports]
  nginx = 8010
  
  [settings]
  document-root = ${buildout:directory}/var/www
  
  [nginx-conf-server]
  file-content =
      ${nginx-fpm-server:servers}
  
  [nginx-fpm-server]
  error_log = ${settings:log-directory}/nginx-phpinfo-error.log
  access_log = ${settings:log-directory}/nginx-phpinfo-access.log
  fastcgi_pass = phpfpm
  nginx-build-location = ${settings:nginx-build-location}

TODO & Questions
----------------

- the strategy for log rotation
- the strategy for data folder
