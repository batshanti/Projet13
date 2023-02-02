FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt
ENV PORT=8000

COPY . /app
EXPOSE $PORT
CMD python manage.py runserver 0.0.0.0:$PORT
