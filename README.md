# Shamseya  Task

## Pre-requisites (On Ubuntu)

- Python 3.6
- docker & docker-compose

## Run

- clone the project
- cd into project's dir
- cp `.env.example` to `.env` and put your values, or use defaults
- `$ docker-compose up` to run postgres container
- `$ manage.py test` to run tests
- `$ manage.py runserver` to run server
- navigate to `http://localhost:8000/api/` to test APIs
- use Postman to test endpoint

## Test from inside VS Code

- make sure [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) is installed
- make sure db container & django server are running
- open the `api.http` file
- make requests and see responses :))
