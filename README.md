# Project Title

Simple demo working through flask-login using session management

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

for unknown reasons. when main.py, auth.py and __init__.py are updated, changes do not appear in browser or print outputs.


python app.py
http://localhost:5000/

```
