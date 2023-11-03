# The base image: Python 3.11 Alpine official image
FROM python:3.11.6-alpine3.18

# The author
LABEL authors="Derfulio"

# set shared environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=1.5.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false

ENV CONTAINER_HOME=/var/www

# set work directory
WORKDIR $CONTAINER_HOME
# We copy our Python requirements here to cache them
# and install only runtime deps using poetry
COPY ./pyproject.toml $CONTAINER_HOME
RUN poetry install --only main  # respects

COPY . $CONTAINER_HOME

# venv already has runtime deps installed we get a quicker install
RUN poetry install

CMD ["uvicorn", "back.main:app", "--host", "0.0.0.0", "--port", "80"]
# If you are running your container behind a TLS Termination Proxy (load balancer) like Nginx or Traefik,
# add the option --proxy-headers, this will tell Uvicorn to trust the headers sent by that proxy telling it that the application is running behind HTTPS, etc.
# CMD ["uvicorn", "back.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]