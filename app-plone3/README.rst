Plone 3.3.5
===========

We need build Plone 3 for some old stuff.

Steps:

* install Python 2.4.6, compile from sources. using
  **python.buildout**.
* install zeocluster using buildout.
* 

Using collective/buildout.python to build python 2.4

Content Migration
-----------------

If you we are using ZODB as the database, the migration will be
as simple as just copy the **Data.fs** file to new Zope instance.

Another choice for migration is using export and import tool
from ZMI.

Steps to reset admin password
-----------------------------

Zope is using the emergency user to reset admin's password.
Here is the steps to reset admin passowrd:

* create a emergency user by using **zpassword.py**.
  The file could be found in utilities folder of Zope installation
* the **zpassword.py** will create a access file for the emergency
  user.
* copy the acces file to Zope instance folder.
* restart the Zope instance and log in using the emergency user.
* the emergency user will be restricted to only access the
  **acl_users** folder.
* reset the admin's password on acl_users.
