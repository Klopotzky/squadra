# <WARNING>
# Everything within sections like <TAG> is generated and can
# be automatically replaced on deployment. You can disable
# this functionality by simply removing the wrapping tags.
# </WARNING>

# <DOCKER_FROM>
FROM python:3
# </DOCKER_FROM>

# <NPM>
# </NPM>

# <BOWER>
# </BOWER>

# <PYTHON>
ENV PYTHONUNBUFFERED=1
WORKDIR /squadra
COPY . /squadra
RUN pip install -r requirements.txt
# </PYTHON>

# <SOURCE>
COPY . /squadra
# </SOURCE>

# <GULP>
# </GULP>

# <STATIC>
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
# </STATIC>

CMD gunicorn --bind=0.0.0.0:9876 --forwarded-allow-ips="*" squadra.wsgi

# *************************************************************************
# potrzebne komendy / DOCKER DESTOP

# docker-compose build
# docker-compose down

# docker-compose run web python manage.py migrate
# docker-compose run web python manage.py createsuperuser
# docker-compose up