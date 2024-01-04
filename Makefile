PYTHON = python
SCRIPT = main.py
VENV = venv

.PHONY: all run clean venv

all: run

run:
	$(PYTHON) $(SCRIPT)

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	call install.bat

clean:
	rmdir /s /q $(VENV)
