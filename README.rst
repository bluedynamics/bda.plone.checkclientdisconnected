Overview
========

This script will check, and if needed restart a zeo-client or many clients given by a config file.
It is meant to be mainly used as a base script for a cronjob to check multiple instances and 
restart them if needed.

Usage
=====

It sets two scripts in the ./bin directory of your egg.
The first script "checksingleclient" takes 2 arguments and restarts the instance if there is an error reaching the zeoserver.

Example::

	$./bin/checksingleclient "/home/user/workspace/project1/bin/instance" "http://127.0.0.1:8080/site" 


The second script checkmulticlient takes a clientlist file and checks every instance given by it.
A default clientlist is in the /etc folder of your egg.

It contains a section: [zeo-clients]

And the given instances should be listed one per line as a tuple like that: 
/pathtoinstance = Address:Port


Example::

	/path/to/plone/bin/instance01 = 127.0.0.1:8080
	/path/to/plone/bin/instance02 = 127.0.0.1:8081
	/path/to/plone2/bin/instance = 127.0.0.1:8180



	$./bin/checkmulticlient etc/clientlist.cfg 


TODO
====



Contributors
============

- Benjamin Stefaner <bs [at] kleinundpartner [dot] at>

- Jens Klein <jk [at] kleinundpartner [dot] at>

