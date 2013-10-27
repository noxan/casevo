TARGET?=development
PYTHON_BIN?=python
VIRTUALENV_BIN?=virtualenv
VIRTUALENV_DIR=env
MANAGE_PY=$(VIRTUALENV_DIR)/bin/python manage.py
PIP_BIN=$(VIRTUALENV_DIR)/bin/pip

export DJANGO_SETTINGS_MODULE=casevo.settings.$(TARGET)


environment:
	test -d "$(VIRTUALENV_DIR)" || $(VIRTUALENV_BIN) --distribute --no-site-packages --python $(PYTHON_BIN) $(VIRTUALENV_DIR)

requirements: environment
	$(PIP_BIN) install -r requirements/base.txt
	$(PIP_BIN) install -r requirements/$(TARGET).txt

database: requirements
	$(MANAGE_PY) syncdb --noinput
	$(MANAGE_PY) migrate --all

serve: server
server: database
	$(MANAGE_PY) runserver 0.0.0.0:8000
