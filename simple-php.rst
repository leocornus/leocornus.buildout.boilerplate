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

Step by step
------------

Here are the steps for how we build the PHP package:

#. clone the boilerplate, update submodule
#. check the dependences for MariaDB, PHP and Nginx,
#. edit the buildout-local.php to fit your local environment
#. bootstrap (python bootstrap.py) the project. boilerplate.
#. build MariaDB
#. build PHP and PHP-FPM, PHP depends on MariaDB
#. build Nginx web server.

Dependences List
''''''''''''''''

TODO: install dependences for different platform.

Local settings
''''''''''''''

TODO: important local setting variables:

- base folder

Build MariaDB
'''''''''''''

Here are the simple steps to build MariaDB::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-mariadb
  $ bin/buildout -N install build-mariadb

Build PHP-FPM
'''''''''''''

Here are the steps to build PHP-FPM::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-php
  $ bin/buildout -N install build-php

Build Nginx
'''''''''''

Here are the steps to build PHP-FPM::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-nginx
  $ bin/buildout -N install build-nginx

Build sys (All in one)
''''''''''''''''''''''

using the include section for all in one superver config::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-sys
  $ bin/buildout -N install build-sys

Questions
---------

- the strategy for configuration files
- the strategy for log files
- the strategy for pid files
- How to generate the all in one supervisord.
  Using the **include** section
