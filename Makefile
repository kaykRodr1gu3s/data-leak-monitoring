.PHONY: install pastefo pastebin

install:
	pip install pipx
	pipx ensurepath
	pipx install poetry
	
	poetry init --no-interaction
	poetry add requests bs4
	poetry add python-dotenv
	poetry add splunk-sdk
	poetry shell

pastefo:
	poetry run python Pastefo/main.py
	rd /s /q Splunk\__pycache__

pastebin:
	poetry run python Pastebin/main.py
	rd /s /q Splunk\__pycache__
