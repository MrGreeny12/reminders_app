# M.A.P.S. (My automated productivity system)
Приложение для личной эффектиности с Open Source лицензией GNU-GPL v.3.

## Потребуются следующие пакеты:
- Docker/Docker-compose
- Python 3.8 и выше

## Порядок установки в локальной сети:
1. Клонировать репозиторий на локальную машину.
2. Установить базовые пакеты ```pip install -r requirements.txt```
3. Запустить сервисы```docker-compose up --build -d```
4. Запустить сервер```python manage.py runserver```


## Порядок установки на сервер:
1. Клонировать репозиторий на сервер.
2. Запустить образ ```sh run.sh``` или ```sudo sh run.sh```


## Запуск тестов:
- ```pytest tests```
