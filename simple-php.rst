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

#. check the dependences for MariaDB, PHP and Nginx,
#. bootstrap (python bootstrap.py) the project. boilerplate.
#. build MariaDB

Dependences List
----------------

Build MariaDB
-------------

Here are the simple steps to build MariaDB::

  $ cd boilerplate
  $ bin/buildout -N -c buildout-init.cfg install init-mariadb
  $ bin/buildout -N install build-mariadb
