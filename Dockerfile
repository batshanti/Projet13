FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt
ENV PORT = 8080

COPY . /app

RUN python manage.py collectstatic --noinput

CMD python manage.py runserver 0.0.0.0:$PORT
