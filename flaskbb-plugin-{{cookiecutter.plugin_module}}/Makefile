.PHONY: clean help test lint format docs dist upload update-translations compile-translations add-translation

help:
	@echo "  clean                  remove unwanted stuff"
	@echo "  test                   run the testsuite"
	@echo "  lint                   check the source for style errors"
	@echo "  format                 sort imports and reformat the code"
	@echo "  docs                   build the documentation"
	@echo "  dist                   creates distribution packages"
	@echo "  upload                 uploads a new version of the wheel package to PyPI"
	@echo "  update-translations    updates the translations"
	@echo "  compile-translations   compiles the translations"
	@echo "  add-translation        adds a new language to the translations"


clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

test:
	pytest

lint:
	ruff check

format:
	ruff check --fix --select I
	ruff check --fix
	ruff format

docs:
	$(MAKE) -C docs html

dist:
	uv build

upload: dist
	uv publish

update-translations:
	pybabel extract -F babel.cfg -k lazy_gettext -o {{ cookiecutter.plugin_module }}/translations/messages.pot .
	pybabel update -i {{ cookiecutter.plugin_module }}/translations/messages.pot -d {{ cookiecutter.plugin_module }}/translations/

add-translation:
	@read -p "Enter new language shortcode:" lang; \
	pybabel init -i {{ cookiecutter.plugin_module }}/translations/messages.pot -d {{ cookiecutter.plugin_module }}/translations/ -l $$lang

compile-translations:
	pybabel compile -d {{ cookiecutter.plugin_module }}/translations/
