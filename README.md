# Тестовое задание Farpost
### Направление: аналитика - python developer
Оригинальное задание имеет ошибку - таблица logs никак не связана с постами, следовательно невозможно определить, к какому посту был сделан комментарий.
Решение: в таблицу logs добавлено поле post_id типа integer

## Использование
Скрипты выполняются из папки ```src```.\
Для инициализации и заполнения баз данных:
```
python create.py
```
Для выгрузки csv файлов:
```
python main.py
```
Для выгрузки csv файлов вводится логин пользователя. Доступные логины:
- user1
- user2

Csv файлы сохраняются в папке ```src/csv```.