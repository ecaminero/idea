#  4Geeks-Odoo-Voip


## Installation

	sudo apt-get update -y	
	sudo apt-get install postgresql postgresql-server-dev-9.3 -y
	sudo apt-get install python-pip python-dev python-ldap libjpeg-dev libevent-dev libxml2-dev node-less libxslt1-dev libldap2-dev libsasl2-dev -y

Creating-user postgresql  -U voip -W voip

http://alacret.blogspot.com/2015/03/postgresql-9x-creating-user-and.html

Problemas en instalar postgresql 9.4?
	http://www.google.com/url?q=http%3A%2F%2Faskubuntu.com%2Fquestions%2F638725%2Finstall-postgres-9-4-on-ubuntu-14-04-2&sa=D&sntz=1&usg=AFQjCNE-KGVH-Zx4MAr6HgcWXYrb-c0fkA

Estos respositorios son super pesados 

	git clone git@github.com:odoo/odoo.git --branch 9.0 --depth 1

	git clone git@gitlab.services4geeks.co:GeeksFactoryOdoo/odoo-9-enterprise.git enterprise


pip requirements  "el box debe tener de memoria ram ≥ 1024"
	
	pip /vagrant/odoo/requirements.txt


## Run

	cd /vagrant/odoo
	./odoo.py -r voip -w voip --addons-path=/vagrant/enterprise/,addons


## Run odoo without enterprise
	python odoo/odoo.py -r voip --addons-path=/vagrant/odoo/addons,/vagrant/modules/