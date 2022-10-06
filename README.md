# Проект 09-22-emphasoft-CRUD

## Описание проекта

API для менеджмента пользователей с авторизацией по токену с развёртыванием в docker-compose

## Установка проекта локально

В папке склонированного репозитория выполните:

```bash
docker-compose up -d --build
docker exec 09-22-emphasoft-crud_emphasoft-crud_1 python3 manage.py collectstatic --noinput
docker exec 09-22-emphasoft-crud_emphasoft-crud_1 python3 manage.py makemigrations
docker exec 09-22-emphasoft-crud_emphasoft-crud_1 python3 manage.py migrate
docker exec -it 09-22-emphasoft-crud_emphasoft-crud_1 python3 manage.py createsuperuser --email admin@admin.com --username admin -v 3
```
Задайте пароль для суперпользователя. Логин суперпользователя - admin.
Для проверки работоспособности, перейдите на localhost/admin

## Пример .env файла

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pass
DB_HOST=db
DB_PORT=5432
SECRET_KEY=p&l%slhtyn^##a1)ilz@4zqj=rq&agdol^##zglmlkmklmewf16w5165^(*U)(&%3dkm9(vs
```

Файл должен находиться в корне проекта

## Документация API

доступна по адресу http://localhost/api/v1/schema/swagger-ui/ при развёрнутом проекте

## Стек

Django, Django REST framework, Docker-compose, Nginx, PostgreSQL, Swagger

## Автор

Семён Егоров  

[LinkedIn](https://www.linkedin.com/in/simonegorov/)  
[Email](rhinorofl@gmail.com)  
[Telegram](https://t.me/SamePersoon)
