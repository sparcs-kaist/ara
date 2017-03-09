NewAra Project
=========================


Import Requirements List
-------------------------

```sh
$ pip install -r requirements.txt
```


Exports Requirements List
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
