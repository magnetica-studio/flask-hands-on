docker-build:
	docker build -t flaskappimage .
docker-run:
	docker run -itd --name flaskapp \
	--mount type=bind,source="$(PWD)",dst=/app \
	-p 5000:5000 \
	flaskappimage
docker-run-db:
	docker run --name test-db -e MYSQL_ROOT_PASSWORD=tmppw -d -p 3306:3306 mysql
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
mysql:
	mysql -h 127.0.0.1 --port 3306  -uroot -p