# Проект 09-22-emphasoft-CRUD

## Описание проекта

API для менеджмента пользователей с авторизацией по токену с развёртывание в docker-compose

## Установка проекта локально

В папке склонированного репозитория выполните:

```bash
docker-compose up -d --build
sudo docker exec 09-22-emphasoft-crud_emphasoft-crud_1 python3 manage.py makemigrations
sudo docker exec 09-22-emphasoft-crud_emphasoft-crud_1 python3 manage.py migrate
docker exec -it 09-22-emphasoft-crud_emphasoft-crud_1 python3 manage.py createsuperuser --email admin@admin.com --username admin -v 3
```
Задайте пароль для суперпользователя. Логин суперпользователя - admin.
```bash
python3 manage.py runserver
```
Для проверки работоспособности, перейдите на localhost/admin

## Документация API

доступна по адресу http://localhost/api/v1/schema/swagger-ui/ при развёрнутом проекте

## Стек

Django, Django REST framework, PostgreSQL, Docker-compose, Swagger

## Автор

Семён Егоров  

[LinkedIn](https://www.linkedin.com/in/simonegorov/)  
[Email](rhinorofl@gmail.com)  
[Telegram](https://t.me/SamePersoon)
