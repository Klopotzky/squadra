# <WARNING>
# Everything within sections like <TAG> is generated and can
# be automatically replaced on deployment. You can disable
# this functionality by simply removing the wrapping tags.
# </WARNING>

# <DOCKER_FROM>
FROM divio/base:4.18-py3.6-slim-stretch
# </DOCKER_FROM>

# <NPM>
# </NPM>

# <BOWER>
# </BOWER>

# <PYTHON>
<<<<<<< HEAD
# z divio # ENV PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/+simple/} \
    # z divio # WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/}
# z divio # COPY requirements.* /app/
# z divio # COPY addons-dev /app/addons-dev/
# z divio # RUN pip-reqs compile && \
    # z divio # pip-reqs resolve && \
    # z divio # pip install \
        # z divio # --no-index --no-deps \
        # z divio # --requirement requirements.urls
FROM python:3
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /squadra/
RUN pip install -r requirements.txt
COPY . /squadra/
# </PYTHON>

# <SOURCE>
COPY squadra_main /app
=======
ENV PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/+simple/} \
    WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/}
COPY requirements.* /app/
COPY addons-dev /app/addons-dev/
RUN pip-reqs compile && \
    pip-reqs resolve && \
    pip install \
        --no-index --no-deps \
        --requirement requirements.urls
# </PYTHON>

# <SOURCE>
COPY . /app
>>>>>>> 8df0496d07d81875516d9350a867ae7830143c26
# </SOURCE>

# <GULP>
# </GULP>

# <STATIC>
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
# </STATIC>
