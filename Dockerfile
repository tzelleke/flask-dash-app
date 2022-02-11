FROM tiangolo/uwsgi-nginx-flask:python3.9
WORKDIR /app
# Install Poetry
RUN apt-get update \
    && apt-get install -y ca-certificates \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false
COPY ./ /app
RUN poetry install --no-root
# STATIC_PATH configures nginx to serve static assets directly
ENV \
    POETRY_HOME=/opt/poetry \
    STATIC_PATH=/app/app/static \
    FLASK_ENV=production
EXPOSE 80