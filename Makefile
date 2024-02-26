static-tests:
	flake8 scripts tables
	pycodestyle scripts tables
	mypy scripts tables

static-tests-docker:
	docker compose build qffun-db-tests
	docker compose run --rm qffun-db-tests make static-tests