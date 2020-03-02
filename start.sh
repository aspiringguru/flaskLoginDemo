# start.sh
#FLASK_APP=name of directory containing __init__.py
export FLASK_APP=project
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_RUN_PORT=8000
export FLASK_RUN_HOST=0.0.0.0
#nbb: 6000 is an unsafe port for chrome (weirdness!)
#next line causes error = ".ror: No such command "run
#flask run
#do flask run manually
