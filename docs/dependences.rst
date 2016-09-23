Dependences libraries
=====================

development tools
-----------------

The development tools will allow us to compile and build software
from source code distribute.

Ubuntu::

  $ aptitude install build-essential git cmake
  $ aptitude install byobu

CentOS::

  $ yum groupinstall 'Development Tools'
  $ yum install cmake
  # we need EPEL repository for CentOS.
  $ yum install epel-release
  $ yum install screen tmux byobu

EPEL_ stands for Extra Packages for Enterprise Linux

Depenencs Libs
--------------

Here are list of libs we need to install.

Ubuntu::

  $ aptitude install libncurses5-dev libcdk5-dev
  $ aptitude install zlib1g-dev
  $ aptitude install libxml2-dev
  # dependence for PHP
  $ aptitude install libgnutls-openssl-dev libssl-dev openssl
  $ aptitude install libcurl4-openssl-dev pkg-config
  $ aptitude install libbz2-dev libxml2-dev gettext
  $ aptitude install libjpeg-dev libpng-dev libgd2-dev
  $ aptitude install libmcrypt-dev libfreetype6-dev
  $ aptitude install libcurl4-openssl-dev libpcre3-dev
  # dependence for MediaWiki
  $ aptitude install curl imagemagick

CentOS:: 

  $ yum install bzip2-devel libjpeg-devel openssl-devel libxml2-devel
  $ yum install libpng-devel libmcrypt-devel freetype-devel gettext
  $ yum install ncurses-devel curl curl-devel

.. _EPEL: https://fedoraproject.org/wiki/EPEL


