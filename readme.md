## Prerequisites

```
docker
docker-compose
```

## Running the server locally

```
- git clone https://github.com/sarimjkhan/voucherpool.git
- docker-compose up

To create the image only, run the following command
- docker-compose --build

open in browser/postman http://localhost:8081
```

## Running the APIS on heroku

```
Access the following url
https://voucherpool.herokuapp.com

You will have the list of general APIs to access.
For other ENDPOINTS, please see the section for documentation and collection at the end.
```

## Running tests

```
Run following command
- python3 manage.py test
```

## CI/CD (GitHub Actions and Heroku)

```
Deployed to HEROKU through GitHub Actions

Please see .github/workflows/main.yml in https://github.com/sarimjkhan/voucherpool.git
```

## API Documentation

```
https://documenter.getpostman.com/view/3727741/UyxbsqWJ
```

**NOTE:** Postman collection is also provided in the `documentation` and is also available in the project's root folder.
