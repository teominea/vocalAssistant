PYTHON = python
SCRIPT = main.py
VENV = venv
ZIPFILE = vocal_assistant.zip  # Name of the zip file

.PHONY: all run clean venvgi

all: run

run:
	$(PYTHON) $(SCRIPT)

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	call install.bat

clean:
	rmdir /s /q $(VENV)

zip_project:
	PowerShell -Command "Compress-Archive -Path .\* -DestinationPath $(ZIPFILE)"