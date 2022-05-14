#!/bin/bash
echo "Starting the application..."
pip install -r requirements.txt
export FLASK_APP=setup.py
flask db init
flask db migrate -m "Migrate Tables"
flask db upgrade
flask run --host=0.0.0.0 --port=80