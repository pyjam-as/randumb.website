
IMGNAME="randumb"

run:
	FLASK_ENV=development \
	pipenv run \
	python randumb.py

check:
	pipenv run \
	mypy --ignore-missing-imports ./


docker-build:
	docker build . -t $(IMGNAME)

docker-run: docker-build
	docker run -p 8080:80 $(IMGNAME)
