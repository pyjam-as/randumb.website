FROM python:3.8

# Force the stdout and stderr streams from python to be unbuffered. See
# https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv gunicorn
WORKDIR /tmp/
COPY ./Pipfile* ./
RUN pipenv install --system

RUN mkdir /app
WORKDIR /app
COPY ./*.py ./

CMD gunicorn --bind 0.0.0.0:80 randumb:app
