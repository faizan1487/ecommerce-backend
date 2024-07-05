FROM python:3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/requirements.txt

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY . /app

CMD python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8000