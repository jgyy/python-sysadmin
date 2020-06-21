python-sysadmin
===============

Read, write, and understand Python code Utilize Python as a primary scripting language Develop Python projects from start to finish Build installable Python packages Use Test Driven Development with Python

pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``https://github.com/jgyy/python-sysadmin.git``
3. Fetch development dependencies: ``make install``

Usage
-----

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make

Running Scripts
---------------

::

    $ python -m pgbackup --driver local ./local-dump.sql postgres://postgres:postgres@127.0.0.1:5432/sample