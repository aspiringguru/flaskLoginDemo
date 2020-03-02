# Project Title

Simple demo working through flask-login using session management
based on
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python 3.7.x

```

### Installing


```
cd /mnt/g/2020_working/coding/flask_auth_DigitalOcean

#windows > G:\2020_working\coding\flask_auth_DigitalOcean

#my default ubuntu login activates conda. ymmv
conda deactivate
#quick test for default version of python
which python3
python3 --version
#python3 -m venv env
source env/bin/activate
(env)$
which python3
python3 --version
pip install flask flask-sqlalchemy flask-login
pip freeze

#setup git repo
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/aspiringguru/flaskLoginDemo.git
git push -u origin master

$list all files in tree structure for easy readability
tree -I env

#create bash script to export environment variables
chmod +x start.sh
#show environment variables
printenv | grep FLASK

#start app. for some reason this fails if in script ugh :(
#NBB: had to adjust the original assignment of FLASK_APP
export FLASK_APP=__init__.py

nb : remove .pyc files from __pycache__/ if need to clear errors.

flask run

http://localhost:5000/
http://localhost:5000/login
http://localhost:5000/signup
http://localhost:5000/logout
http://localhost:5000/profile
```
version with templates added.
https://github.com/aspiringguru/flaskLoginDemo/tree/f20ca2e9efb7f0c7a66bffdb83a3f40e4261549e
now setup the database.
```
from project import db, create_app
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
```
within __init__.py
```
db = SQLAlchemy()
def create_app():
```
the code
```
from project import db
```
imports project/__init__.py which initializes object db

this creates the sqlite database file db.sqlite defined in __init__.py

- command line access sqlite3 datbase
sqlite3 project/db.sqlite
- list tables
.tables

https://www.sqlitetutorial.net/sqlite-tutorial/sqlite-show-tables/
https://flask-login.readthedocs.io/en/latest/


to setup access from external domain ie.
http://bmatthewtaylor.duckdns.org/
on router - setup port forwarding.
192.168.1.1 > virtual servers
login to duckdns.org
confirm current external ip is registered on duckdns
check flask port matches virtual server (exports in start.sh)


todo : bootstrap to make fit on various device sizes.
display data after login
add foreign key referenced table
collect data from another source
