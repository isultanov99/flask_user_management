# User management panel with Flask

## Description — Описание

The `Flask` user management panel app with `PostgreSQL` database.\
There are two kinds of users: superusers and ordinary users.\
Ordinary users can only view the list of users, superusers have the ability to edit and delete existing users and create new ones.

---
Приложение для управления пользователями `Flask` с базой данных `PostgreSQL`.\
Имеется два типа пользователей: суперпользователи и обычные пользователи.\
Обычные пользователи могут только просматривать список пользователей, суперпользователи имеют возможность редактировать и удалять существующих пользователей и создавать новых.

## Getting Started — Начало работы

First of all, set up environment variable `DATABASE_URL` with connection string URI of your `PostgreSQL` DB using the format defined in the [documentation](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING).

---

Первым делом настройте переменную среды `DATABASE_URL` с адресом вашей БД `PostgreSQL` в формате, изложенном в [документации](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING).

---

macOS (Tested on macOS Mojave 10.14)
```bash
$ git clone https://github.com/isultanov99/flask_user_management.git
$ cd flask_user_management/
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ flask db migrate
$ flask db upgrade
```

Linux (Tested on Ubuntu 21.10 and WSL Ubuntu 18.04)
```bash
$ git clone https://github.com/isultanov99/flask_user_management.git
$ cd flask_user_management/
$ pip install virtualenv
$ python -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python -m flask db migrate
$ python -m flask db upgrade

```

Windows (Tested on Windows 10 ver. 20H1)

```cmd
git clone https://github.com/isultanov99/flask_user_management.git
cd flask_user_management
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python -m flask db migrate
python -m flask db upgrade
```

## Configure and running the app — Настройка и запуск приложения

Launch app:
```bash
$ python app.py
```
and go to [http://localhost:5000/](http://localhost:5000/), and log in with `admin:admin`.\
If you are running into `import` errors, try `pip3` and `python3` instead of `pip` and `python`.

---
Запустите приложение:
```bash
$ python app.py
```
Перейдите по ссылке [http://localhost:5000/](http://localhost:5000/) и войдите, используя имя пользователя и пароль `admin:admin`. \
Если вы столкнулись с `import` ошибками, попробуйте `pip3` и `python3` вместо `pip` и `python`.
