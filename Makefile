.PHONY: install pastefo pastebin

ifeq (($(OS)), Windows_NT)
install:
	pip install pipx
	pipx ensurepath
	pipx install poetry
	poetry init --no-interaction
	poetry add requests bs4
	poetry install

pastefo:
	poetry run python Pastefo/main.py

pastebin:
	poetry run python Pastebin/main.py

else
install:
	pip install pipx
	pipx ensurepath
	pipx install poetry
	poetry init --no-interaction
	poetry add requests bs4
	poetry install

pastefo:
	poetry run python3 Pastefo/main.py

pastebin:
	poetry run python3 Pastebin/main.py

endif