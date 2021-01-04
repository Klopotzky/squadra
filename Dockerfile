FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /squadra
COPY requirements.txt /squadra/
RUN pip install -r requirements.txt
COPY . /squadra/

#RUN DJANGO_MODE=build python manage.py collectstatic --noinput