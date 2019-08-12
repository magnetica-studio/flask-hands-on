docker-build:
	docker build -t flaskappimage .
docker-run:
	docker run -itd --name flaskapp \
	--mount type=bind,source="$(PWD)",dst=/app \
	-p 5000:5000 \
	flaskappimage
docker-logs:
	docker logs -f flaskapp
lint:
	docker exec flaskapp flake8 ./**/*.py
lint-fix:
	docker exec flaskapp autopep8 --in-place --aggressive --aggressive ./**/*.py;
type-check:
	docker exec flaskapp mypy ./**/*.py
test:
	docker exec flaskapp pytest
