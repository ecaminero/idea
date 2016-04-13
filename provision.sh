#!/bin/bash
echo "update & upgrade"
sudo apt-get update && apt-get upgrade -y

echo "install server-dev-9.4"
sudo apt-get install postgresql-9.3 postgresql-server-dev-9.3 -y
sudo apt-get install postgresql-client-common
echo "pip python-dev node-less libxml2"
sudo apt-get install python-pip python-dev python-ldap libjpeg-dev libevent-dev libxml2-dev node-less libxslt1-dev libldap2-dev libsasl2-dev libpq-dev -y 

echo Visit: http://alacret.blogspot.com/2015/03/postgresql-9x-creating-user-and.html


