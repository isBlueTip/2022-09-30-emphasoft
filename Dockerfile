FROM python:3.9-slim-bullseye

RUN mkdir /app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY emphasoft_crud/ /app
WORKDIR /app
CMD ["gunicorn", "emphasoft_crud.wsgi:application", "--bind", "0:8000" ]
