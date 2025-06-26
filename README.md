# Flask Redis Demo

This project provides a simple Flask application that uses Redis to track page visits. It ships with a `docker-compose.yml` configuration for easy setup.

## Prerequisites
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

## Cloning the Repository
```
 git clone <repo-url>
 cd flask-redis-demo
```
Replace `<repo-url>` with the URL of this repository.
## Running with Docker Compose
From the project directory, run:
```
docker-compose up --build
```
This builds the application image and starts both the Flask app and a Redis container. Once the services are running, visit `http://localhost:5000` in your browser.

## Closing with Docker Compose
To stop the Docker use:
```
docker-compose down
```
Thie automaticly stops the Docker Image and removes it
