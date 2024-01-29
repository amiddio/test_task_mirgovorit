# Test Task Mirgovorit

## Стэк

`Python 3.10`, `Django 5`, `Docker`

## Управление

### Сборка проекта

* Создайте директорию (например: `d:/test_task_mirgovorit`)
* Откройте консольную программу и перейдите в созданную директорию (например: `PowerShell` и `cd d:/test_task_mirgovorit`)
* Клонируйте проект с репозитория: `git clone https://github.com/amiddio/test_task_mirgovorit.git .`
* Запустите Docker
* С корня `d:/test_task_mirgovorit` запустите: `docker-compose build`

### Запуск

* Перейдите в корень проекта `d:/test_task_mirgovorit`
* Выполните команду: `docker-compose up`
* Тестировать можно по урл-у: `http://localhost:8000`

### Остановка

* С корня `d:/test_task_mirgovorit` выполните команду `docker-compose down`

## Тестирование

Для удобства я положил в репозиторий `db.sqlite3` в которой создан админ, несколько продуктов и рецепов

### Админ панель

http://localhost:8000/admin/
* user: admin
* password: qwerty

### GET add_product_to_recipe

http://localhost:8000/add_product_to_recipe/3/13/5
* 3 - рецепт id
* 13 - продукт id
* 5 - кол-во грамм

### GET cook_recipe

http://localhost:8000/cook_recipe/3
* 3 - рецепт id

### GET show_recipes_without_product

http://localhost:8000/show_recipes_without_product/8
* 8 - продукт id

Логика отображения: продукт Сыр есть в рецепте Паста (9гр), есть в Сырниках (10гр) и нет в Фри. 
Следовательно, согласно условию задачи, в таблицу выводим Пасту и Фри.

![Screenshot_1](/screenshots/Screenshot_1.png)
