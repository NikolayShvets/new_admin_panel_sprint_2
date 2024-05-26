FROM python:3.12

WORKDIR /opt/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DJANGO_SETTINGS_MODULE "config.settings"

COPY /requirements/base.txt requirements.txt
RUN apt update && pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000
