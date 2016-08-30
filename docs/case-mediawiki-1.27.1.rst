Case Study MediaWiki upgrade 1.27.0 to 1.27.1
=============================================

Track the steps to migrate MediaWiki from 1.27.0 to 1.27.1.

This upgrade is only MeidaWiki core code upgrade.
It might also require some entensions upgrade too.
But overall, it should be a minor upgrade.

Upgrade Strategy
----------------

As we are using de-centralism way to manage buildout config files,
it is very easy to create a new build for MediaWiki and WordPress.
Here are the brief steps:

* rename the existing app folder as backup, app-wpmw -> app-wpmw-1.27.0
* create a new app foler for newer version, app-wpmw
* initialize /bootstrap buildout
* update MediaWiki version information.
* execute buildout
* execute update maintenance script
* restart server and test...
