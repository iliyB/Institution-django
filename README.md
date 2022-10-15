## Инструкция по развертке проекта

1) Скопировать содержимой .env.example в .env
```
cp .env.example .env
```
2) Заполнить недостающие переменные в .env
3) Сбилдить проект
```
make build
```
4) Запустить проект
```
make up
```
5) Произвести миграции в БД
```
make migrate
```
6) Создать суперпользователя с паролем из .env DJANGO_SUPERUSER_PASSWORD
```
make make createsuperuser username=admin email=admin@mail.ru
```

## Дополнительно

* Создать новые миграции
```
make makemigrations
```
* Запустить тесты
```
make test
```
* Установить линтеры
```
make precommit-install
```
* Проверь проект линтерами
```
make lint
```