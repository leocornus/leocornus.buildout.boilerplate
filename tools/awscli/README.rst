AWS Command Line Interface
==========================

The comprehensive command line interface to manipulate AWS services,
including:

* s3

configuration
-------------

The command configure will be used to configure AWS command line::

  bin/aws configure list
  bin/aws configure --profile mytest list

Using different profile for s3 command::

  bin/aws --profile mytest s3 sync
