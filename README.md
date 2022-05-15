# iban-validator

This repo contains a web server and REST API for validating IBAN numbers.

The REST API is built using FastAPI, and has one endpoint 

> GET api/v1/iban-validation/{iban}

which validates the IBAN number given in "{iban}"


# Requirements

This app requires Docker and optionally docker-compose.


# App

If using docker-compose, the app Docker image can built by running

> docker-compose build

and then started by running

> docker-compose up app


If using Docker, the app image can be built by running

> docker build -t iban-validator-app .

and then started by running

> docker run -it -p 8080:80 iban-validator-app


In both cases above, the API can then be accessed on port 8080

