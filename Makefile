TARGET?=development
PYHON_BIN=python
VIRTUALENV_DIR=env
MANAGE_PY=$(VIRTUALENV_DIR)/bin/python manage.py
PIP_BIN=$(VIRTUALENV_DIR)/bin/pip

export DJANGO_SETTINGS_MODULE=casevo.settings.$(TARGET)


environment:
	test -d "$(VIRTUALENV_DIR)" || $(VIRTUALENV_BIN) --distribute --no-site-packages --python $(PYTHON_BIN) $(VIRTUALENV_DIR)

server:
	$(MANAGE_PY) runserver 0.0.0.0:8000
