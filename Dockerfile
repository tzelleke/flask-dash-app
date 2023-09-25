ARG PYTHON_VERSION=3.11
ARG POETRY_VERSION=1.6
ARG UID=1000
ARG GID=1000
ARG USER=app

FROM tiangolo/uwsgi-nginx-flask:python${PYTHON_VERSION} as base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_IGNORE_INSTALLED=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app
ENV STATIC_PATH=/app/app/static

FROM base as poetry
# Install poetry
ARG POETRY_VERSION
ENV POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false
RUN pip install --upgrade --quiet pip \
    && python -m venv ${POETRY_HOME} \
    && ${POETRY_HOME}/bin/pip install --upgrade --quiet \
    poetry==${POETRY_VERSION} \
    && ln -s ${POETRY_HOME}/bin/poetry /usr/local/bin/poetry \
    && poetry self add poetry-plugin-up \
    && poetry --version
COPY pyproject.toml poetry.lock* ./
RUN poetry install --only main --no-root --no-interaction --no-ansi

FROM poetry as dev
# install sudo
RUN apt-get update \
    && apt-get install -y --no-install-recommends sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Create dedicated user, add to sudoers
ARG USER
ARG UID
ARG GID
RUN groupadd -g ${GID} ${USER} \
    && useradd \
    --no-log-init \
    --create-home \
    --shell /bin/bash \
    --uid ${UID} \
    --gid ${GID} \
    ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && getent passwd ${USER}
RUN poetry install --no-root --no-interaction --no-ansi
COPY . .

FROM base as prod
ARG PYTHON_VERSION
COPY --from=poetry \
    /usr/local/lib/python${PYTHON_VERSION}/site-packages \
    /usr/local/lib/python${PYTHON_VERSION}/site-packages
COPY . .
