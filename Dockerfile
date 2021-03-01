FROM python:3.8

RUN apt-get update -y && apt-get upgrade -y

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --upgrade pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /app/

CMD ["gunicorn", "--preload", "--bind=0.0.0.0:8080", "--log-level=debug", "weather.wsgi"]