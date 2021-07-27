FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./ /app
RUN apt-get update \
    && apt-get install -y ca-certificates \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && /root/.poetry/bin/poetry config virtualenvs.create false \
    && /root/.poetry/bin/poetry install --no-interaction --no-ansi
# STATIC_PATH configures nginx to serve static assets directly
ENV \
    STATIC_PATH /app/app/static \
    FLASK_ENV production
EXPOSE 80