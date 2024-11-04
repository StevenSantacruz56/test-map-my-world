FROM python:3.10

ENV TZ="America/Bogota"

WORKDIR /app

# Install Poetry
RUN pip install poetry

# We copy only the requirements.txt first to leverage Docker cache
COPY pyproject.toml ./
COPY poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi


RUN apt-get update && apt-get install -y locales && \
    echo "es_ES.UTF-8 UTF-8" > /etc/locale.gen && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=es_ES.UTF-8

ENV LANG es_ES.UTF-8

COPY . /app
WORKDIR /app
EXPOSE 80

ENTRYPOINT python3 -m gunicorn --threads=2 map_my_world.src.ports.rest.main:app --bind 0.0.0.0:80 -k uvicorn.workers.UvicornWorker --timeout 3600
