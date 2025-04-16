#!/bin/sh

sleep 20  # wait for DB to be ready
mysql -h data -u root -proot < /opt/mydatabase.sql

