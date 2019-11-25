
IMGNAME="randumb"

run:
	FLASK_ENV=development \
	pipenv run \
	python randumb.py


docker-build:
	docker build . -t $(IMGNAME)

docker-run:
	docker run $(IMGNAME)
