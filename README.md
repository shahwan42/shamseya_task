# Shamseya  Task

## Pre-requisites (On Ubuntu)

- Python 3.6
- docker & docker-compose

## Run

- clone the project
- cd into project's directory
- create a python virtualenv and activate it (choose one of the following approaches)
  - `$ python -m venv .venv && source .venv/bin/activate`
  - `$ mkvirtualenv shamseya-task`
  - `$ poetry install && poetry shell` (will automatically create a venv and install the deps (needs poetry installed), skip following 2 steps after this approach)
- `$ python -m pip install poetry`
- `$ poetry install` install project dependencies inside the venv
- `$ cp .env.example .env`
- `$ docker-compose up` to run postgres container
- `$ ./manage.py test` to run tests
- `$ ./manage.py migrate` to apply migrations
- `$ ./manage.py loaddata all_data.db` to load my data to test on
- `$ ./manage.py runserver 8005` to run server
- navigate to `http://localhost:8005/api/core/reviews/` to open in the browser (Make sure you're logged-in)
- Or use Postman to test the endpoint (provide Basic Auth: user&pass)

## Available users

- usernames: `super_user`, `staff_user`, `active_user`
- password (same for all): `Awesome1`

## Authentication routes

- `/api/auth/login/`
- `/api/auth/logout/`

## More commands

- `$ ./manage.py populate_db` add sample db records (takes time)
- `$ ./manage.py clean_db` remove all db entries

## Test from inside VS Code

- make sure [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) is installed
- make sure db container & django server are running
- open the `api.http` file
- make requests and see responses :))

## Thank you
