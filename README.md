# Шаблон Django-проекта для VPS (в Docker)
## Потребуются следующие пакеты:
- Docker/Docker-compose
- Django v.3.2 и выше
- Python 3.8 и выше

## Порядок установки:
1. Нажать кнопку в правом углу "Use this template".
2. Клонировать репозиторий на локальную машину.
3. Отредактировать файлы ```Dockerfile, docker-compose.yml, nginx.conf```
4. Установить базовые пакеты ```pip install -r requirements.txt```
5. Запустить образ ```sh run.sh``` или ```sudo sh run.sh```