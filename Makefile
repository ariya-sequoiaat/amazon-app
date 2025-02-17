# Makefile
.PHONY: setup test clean build run

setup:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	python amazon_cli/main.py

test:
	pytest -v tests/test_amazon_scraper.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +











# # Makefile
# .PHONY: setup test clean build run
#
# setup:
# 	python -m pip install --upgrade pip
# 	pip install -r requirements.txt
#
# test:
# 	pytest -v
#
# clean:
# 	find . -type d -name "__pycache__" -exec rm -r {} +
# 	find . -type f -name "*.pyc" -delete
# 	find . -type f -name "*.pyo" -delete
# 	find . -type f -name "*.pyd" -delete
# 	find . -type d -name "*.egg-info" -exec rm -r {} +
# 	find . -type d -name "*.egg" -exec rm -r {} +
# 	find . -type d -name ".pytest_cache" -exec rm -r {} +
#
# build:
# 	docker build -t amazon-scraper .
#
# run:
# 	docker run amazon-scraper