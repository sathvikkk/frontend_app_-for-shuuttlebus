FROM python:3-alpine3.13

WORKDIR /app

COPY . /app

RUN pip install flask
RUN pip install flask_mysqldb

EXPOSE 5000

CMD ["python3", "app.py"]