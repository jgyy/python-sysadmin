#!/bin/sh

pip install --user virtualenv
mkdir venvs
virtualenv venvs/pg
source venvs/pg/bin/activate
pip install psycopg2
