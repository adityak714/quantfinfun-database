static-tests:
	pylint scripts tables data_models utils
	flake8 scripts tables data_models utils
	pycodestyle scripts tables data_models utils 
	mypy scripts tables data_models utils

static-tests-docker:
	docker compose build qffun-db-tests
	docker compose run --rm qffun-db-tests make static-tests

setup-database:
	docker compose up -d database
	docker compose up -d adminer


format-code:
	black --line-length 75 scripts utils tables data_models
	isort --line-length 75 scripts utils tables data_models