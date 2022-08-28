lint:
	mkdir -p reports
	touch reports/pylint.txt;
	chmod -R 777 reports/
	isort app tests --check
	black app tests --check
	pylint app tests | tee reports/pylint.txt
	mypy app tests --txt-report reports

test:
	pytest -v --cov=app
