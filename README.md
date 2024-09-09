# EduPort Django Rest Framework Backend

This is a private repository for the EduPort backend system.

# Steps to work with the repo

- Clone the repo
```shell
  git clone <repo_url>
  cd <repo_directory>
```

- Install poetry package manager (https://python-poetry.org/docs/#installation)
- Setup a Postgres database however you would like eg: Docker, brew, etc
- Setup a .env file at the root of the project with the following variables:

```shell
#DB SETUP
  DB_NAME=eduport
  DB_USER=db_username
  DB_PASSWORD=password
  DB_HOST=localhost
  DB_PORT=5432

# Django Secrete key
  SECRET_KEY=yoursecretkey

# email host setup
  HOST_MAIL = host mail
  HOST_PASSWORD = app_password

```
Ensure that the database is created and the user has the required permissions.

- To install dependencies:
```shell
    poetry install
```

- To activate virtual environment:
```shell
    poetry shell
```

- To Run Migrations:

```shell
  python manage.py makemigrations
  python manage.py migrate

```

- To import necessary data:
```shell
  python manage.py import_qualifications
  python manage.py import_state_and_countries
```

- To run the server
```shell
  python manage.py runserver
```

- If you want to add any dependencies run:
```shell
  poetry add <package>
```

- To created super user:
```shell
  python manage.py createsuperuser
``` 


 If you are pulling the lastest code which you have already working on please run these cammands

 

