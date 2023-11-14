FROM python:3.11-slim AS base
LABEL maintainer="Ana Cândida Pereira de Quadros acandida.quadros@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /code/


COPY pyproject.toml /code/
RUN pip install --no-cache-dir poetry==1.6.1 && \
    poetry config virtualenvs.create false

COPY . /code/

# DEV
FROM base AS dev
RUN poetry install --no-root
WORKDIR /code/imdb_crawler
# ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["python", "run_spider.py"]


# PROD
FROM base AS release
RUN poetry install --no-dev --no-root
WORKDIR /code/imdb_crawler
# ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["python", "run_spider.py"]


