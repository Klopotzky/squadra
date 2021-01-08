# <WARNING>
# Everything within sections like <TAG> is generated and can
# be automatically replaced on deployment. You can disable
# this functionality by simply removing the wrapping tags.
# </WARNING>

# <DOCKER_FROM>
FROM debian:8.7
# </DOCKER_FROM>

# <NPM>
# </NPM>

# <BOWER>
# </BOWER>

# <PYTHON>
ENV PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/aldryn-baseproject/+simple/} \
    WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/aldryn-baseproject/}
COPY requirements.* /squadra/
COPY addons-dev /squadra/addons-dev/
RUN pip install \
        --no-index --no-deps \
        --requirement requirements.urls
# </PYTHON>

# <SOURCE>
COPY . /squadra
# </SOURCE>

# <GULP>
# </GULP>

# <STATIC>
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
# </STATIC>
