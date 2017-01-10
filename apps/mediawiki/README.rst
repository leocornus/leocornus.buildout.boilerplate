Standalone MediaWiki site
=========================

Boilerplate for building a standalone MediaWiki site.

Here are the basic components:

* php-fpm
* Nginx virtual server
* MariaDB database server and database users.
* MediaWiki source code
* Parsoic service / Node.js
* ElasticSearch / Java infrastructure

MediaWiki configruation
-----------------------

* wiki site configuration.
* Nginx server configuration, including the php-fpm settings
* connection to MariaDB
* connection to Parsoid serivce
* connection to Elastic search service

Application customization
-------------------------

* set to load the login page directly if user not logged in.
* Homepage to list some cool thing.

Tools
-----

* script to create database and database users
* script to refresh the demo site every week.
