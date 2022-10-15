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