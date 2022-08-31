FROM python:3.10-slim-buster

ENV APP_HOME=/server

ENV PYTHONPATH=${APP_HOME} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && apt-get install git curl gcc -y
WORKDIR $APP_HOME

COPY . $APP_HOME

RUN curl -sSL https://install.python-poetry.org/ | python3 - \
    && export PATH="/root/.local/bin:$PATH" \
    && poetry config virtualenvs.create false \
    && pip install --upgrade pip && \
    if [ "$ENV_TYPE" = 'Production' ]; \
    then \
        poetry install --no-dev; \
    else \
        poetry install; \
    fi

EXPOSE 8001

