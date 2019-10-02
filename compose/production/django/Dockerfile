FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi

COPY ./compose/production/django/entrypoint /entrypoint
COPY ./compose/production/django/start /start
COPY ./compose/production/django/celery/worker/start /start-celeryworker
COPY ./compose/production/django/celery/beat/start /start-celerybeat
COPY ./compose/production/django/celery/flower/start /start-flower

RUN \
  # set up user
  addgroup -S django && adduser -S -G django django \
  \
  # set up entrypoint
  && sed -i 's/\r//' /entrypoint \
  && chmod +x /entrypoint \
  && chown django /entrypoint \
  \
  # set up start
  && sed -i 's/\r//' /start \
  && chmod +x /start \
  && chown django /start \
  \
  # set up start-celeryworker
  && sed -i 's/\r//' /start-celeryworker \
  && chmod +x /start-celeryworker \
  && chown django /start-celeryworker \
  \
  # set up start-celerybeat
  && sed -i 's/\r//' /start-celerybeat \
  && chmod +x /start-celerybeat \
  && chown django /start-celerybeat \
  \
  # set up start-flower
  && sed -i 's/\r//' /start-flower \
  && chmod +x /start-flower

# cache requirements
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt

# you may want to consider this, however need to figure out how to serve media files
# COPY . /app
# RUN chown -R django /app
# USER django

WORKDIR /app
ENTRYPOINT ["/entrypoint"]
