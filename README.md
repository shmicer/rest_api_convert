# DRF Currency Converter

A simple Django Rest Framework application for currency conversion.


## Description

- Currently there are 7 currencies available for conversion: ['AED', 'USD', 'EUR', 'RUB', 'TRY', 'CNY', 'HKD'].
- Courses are requested from the service https://currencyapi.com/
- In order to reduce the number of requests to a third-party service, the data received from the service is cached in Redis every 24 hours.
- A request for current courses is made using a deferred task in Celery on a schedule once every 24 hours.


## Quick Start

Clone this repository to your local machine and rename the `.env.example` file found in the root directory of the project to folder `.envs/local/.django` and update the environment variables accordingly. Then you can start the project using Docker or manually using virtual environment.

Using Docker:

```
$ docker compose -f local.yml build

$ docker compose -f local.yml up

```

Open a browser and go to http://localhost:8000


