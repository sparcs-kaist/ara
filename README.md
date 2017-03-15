NewAra Project
=========================


Import Requirements List
-------------------------

```sh
$ pip install -r requirements.txt
```


Export Requirements List
-------------------------

```sh
$ pip freeze > requirements.txt
```


Create/Update Database Tables
-------------------------

At first, Put `config` directory into `ara/ara/settings`.
You can get these files from project master.

```sh
$ python manage.py migrate
```

Dump Fixtures
-------------------------

```sh
$ python manage.py loaddata user.json
$ python manage.py loaddata user_profile.json
$ python manage.py loaddata category.json

```