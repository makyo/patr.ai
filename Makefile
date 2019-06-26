VENV ?= venv

.PHONY: run
run: $(VENV)/bin/django-admin
	venv/bin/python patrai/manage.py runserver_plus

$(VENV)/bin/python:
	virtualenv $(VENV) --python=`which python3`
	$(VENV)/bin/pip install -r requirements.txt
