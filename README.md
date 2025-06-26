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

## Running Locally Without Docker
Alternatively, you can run the application directly on your machine:
1. Install Python 3.10 or newer.
2. Install dependencies:
   ```
   pip install -r app/requirements.txt
   ```
3. Ensure a Redis server is available (locally or on the network).
4. Set the environment variable `REDIS_HOST` if your Redis server isn't running on `localhost`.
5. Start the application:
   ```
   python app/app.py
   ```

Now open `http://localhost:5000` to see the page counter in action.
