from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port="6379")

@app.route("/ping")
def foo():
    print("hit ping route")
    return {"status": "ok"}


@app.route("/count")
def counter():
    print("hit counter route again")
    redis.incr("counter")
    return {"count": str(redis.get("counter"), 'utf-8')}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
