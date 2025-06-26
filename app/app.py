from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

@app.route("/")
def hello():
    try:
        r.incr("visits")
        visits = r.get("visits").decode()
    except redis.exceptions.RedisError as e:
        app.logger.error(f"Redis error: {e})
        visits = "unknown"
    
    return f"Hello! You have visited this page {visits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
