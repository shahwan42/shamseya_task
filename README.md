# Shamseya  Task

## Pre-requisites (On Ubuntu)

- Python 3.6
- docker & docker-compose

## Run

- clone the project
- cd into project's dir
- create a python virtualenv and activate it
- `$ cp .env.example .env`
- `$ docker-compose up` to run postgres container
- `$ ./manage.py test` to run tests
- `$ ./manage.py migrate` to apply migrations
- `$ ./manage.py loaddata core` to load initial data
- `$ ./manage.py runserver 8005` to run server
- navigate to `http://localhost:8005/api/core/reviews/` to open in the browser
- Or use Postman to test the endpoint

## More commands

- `$ ./manage.py populate_db` add sample db records (takes time)
- `$ ./manage.py clean_db` remove all db entries

## Test from inside VS Code

- make sure [REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) is installed
- make sure db container & django server are running
- open the `api.http` file
- make requests and see responses :))
