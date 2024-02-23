static-tests:
	flake8 scripts tables
	pycodestyle scripts tables
	mypy scripts tables

static-tests-docker:
	docker compose build qffun-static-test  
	docker compose run --rm qffun-static-test make static-tests