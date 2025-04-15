from flask import Flask
app = Flask(__name__)

@app.route("/ping")
def foo():
    print("hit ping route")
    return {"status":"ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)