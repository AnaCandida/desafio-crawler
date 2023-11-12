FROM python:3.12-slim AS base
LABEL maintainer="Ana Cândida Pereira de Quadros acandida.quadros@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /code


COPY pyproject.toml /code/
RUN pip install --no-cache-dir poetry==1.6.1 && \
    poetry config virtualenvs.create false


FROM base AS dev

RUN poetry install --no-root
COPY . /code/
ENTRYPOINT ["tail", "-f", "/dev/null"]

FROM base AS release

RUN poetry install --no-dev --no-root

COPY . /code/

ENTRYPOINT ["tail", "-f", "/dev/null"]


