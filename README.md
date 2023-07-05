# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Установите виртуальное окружение командой 
```
python -m venv venv
```
- Установите зависимости командой 
```
pip install -r requirements.txt
```
- Запустите сайт командой
```
python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
- Добавьте файл `.env`.
- Укажите название файла с исходными данными
```
DATA_FILE = 'имя_файла.xlsx'
```

## Данные для отображения на сайте

- Данные содержатся в файле `wine.xlsx`.
- Чтобы изменить данные - внесите изменения в файл и сохраните.
  
Таблица может содержать произвольное количество строк с данными. Для каждой строки обязательно указать категорию и название.
Название колонок изменять запрещено.



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
