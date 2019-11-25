
FROM python:3.8

RUN pip install pipenv gunicorn
WORKDIR /tmp/
COPY ./Pipfile* ./
RUN pipenv install --system

CMD gunicorn --bind 0.0.0.0:80 randumb:app
