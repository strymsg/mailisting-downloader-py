PYTHON=python3
VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make download-debian"
	@echo "     Downloads emails from debian mailinglist reading debian-mailinglist.yaml config file"
	@echo "make compress"
	@echo "     Creates a tar.gz file of downloaded files (output directory)"
	@echo "make csv-debian"
	@echo "     Creates a single csv file of the debian mailinglist donwloaded files, this one is usefull in order to do data analysis from the csv file"
	@echo "make nuke"
	@echo "     Deletes all contents of output directory of donwloaded files"
	@echo "make install"
	@echo "     Install python dependencies"
	@echo "make prepare-dev"
	@echo "     Install system dependencies"
prepare-dev:
	sudo apt-get -y install python3 python3-pip
	python3 -m pip install virtualenv
	make install

install:
	( \
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME); \
        $(VENV_ACTIVATE); \
	pip install -r requirements.txt; \
	)

download-debian:
	( \
	$(VENV_ACTIVATE); \
	python debian-mailinglist.py; \
	)

compress:
	tar cvfz output.tar.gz output

csv-debian:
	( \
	$(VENV_ACTIVATE); \
	python utils/debianMailinglistToCsv.py; \
	)

nuke:
	rm -rf output/*
