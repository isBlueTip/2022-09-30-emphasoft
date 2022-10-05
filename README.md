# Проект 09-22-emphasoft-CRUD

## Описание проекта

API для менеджмента пользователей с авторизaцией по токену

## Установка проекта локально

В папке склонированного репозитория выполните:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd emphasoft_crud
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --email root@root.com --username root -v 3
```
Задайте пароль для суперпользователя. Логин суперпользователя - root.
```bash
python3 manage.py runserver
```
Для проверки работоспособности, перейдите на localhost/admin

## Документация API

доступна по адресу http://localhost:8000/api/v1/schema/swagger-ui/ при развёрнутом проекте

## Стек

Django, Django REST framework, SQLite, Swagger

## Автор

Семён Егоров  

[LinkedIn](https://www.linkedin.com/in/simonegorov/)  
[Email](rhinorofl@gmail.com)  
[Telegram](https://t.me/SamePersoon)
