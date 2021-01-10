# <DOCKER_FROM>
FROM python:3
# </DOCKER_FROM>

# <PYTHON>
ENV PYTHONUNBUFFERED=1
WORKDIR /squadra
COPY . /squadra
RUN pip install -r requirements.txt
# </PYTHON>

# <SOURCE>
COPY . /squadra
# </SOURCE>

# <STATIC>
RUN python manage.py collectstatic --noinput
# </STATIC>

EXPOSE 8001 8001

CMD gunicorn --bind=0.0.0.0:8001 --forwarded-allow-ips="*" squadra.wsgi

# *************************************************************************
# potrzebne komendy / DOCKER DESTOP
# *************************************************************************

# docker-compose build          : buduje obrazy kontenerow
# docker-compose down           : zatrzymuje wszystkie kontenery

# docker exec -it squadra_web_1 python manage.py i_tu_to_co_chcę_wywołać
# makemigrations, migrate, createsuperuser

# docker logs squadra_web_1     : pokazuje logi wybranego okntenera
# docker-compose up db          : podnosi odpowiedni kontener "db"
# docker-compose up -d web      : podnosi w tle (-d) odpowiedni kontener "web"

# docker-compose ps             : pokazuje kontenery i ich status
# docker-compose logs           : pokazuje wszystkie logi

# docker restart squadra_web_1  : restart kontenera
# docker volume ls              : pokazuje wszystkie volume
# docker volume prune           : usuwa wszystkie nieuzywane volume
# docker images -a              : pokazuje wszystkie obrazy
# docker image prune            : usuwa wszystkie 'zwisajace' obrazy

# docker rm                     : usuwa

# *************************************************************************
# odpalanie dockera
# *************************************************************************
#
# docker-compose build
# docker-compose up -d db
# docker-compose up -d web
# docker exec -it squadra_web_1 python manage.py migrate
# docker exec -it squadra_web_1 python manage.py createsuperuser