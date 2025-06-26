# This script starts a Flask (web) application connected to Redis to count page visits
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)  # connect to Redis service from docker-compose, "redis" is the hostname of the Redis container in docker-compose.ymal

@app.route("/")
def hello():
    try:
        # increment the visit count in Redis
        r.incr("visits")
        visits = r.get("visits").decode()
    except redis.exceptions.RedisError as e:
        # log the error and display 'unkown' if Redis is unavailable
        app.logger.error(f"Redis error: {e}")
        visits = "unknown"  
    return f"Hello! You have visited this page {visits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
