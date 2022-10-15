FROM python:3.10

ENV POETRY_VERSION=1.1.12
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
ARG ENV

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p /src/

RUN apt-get update \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry install $(if test "$ENV" = prod; then echo "--no-dev"; fi)

WORKDIR /src
COPY src/ /src/

ENV DJANGO_SETTINGS_MODULE=configs.settings