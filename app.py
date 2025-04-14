import flask
app = flask(__name__)

@app.route("/ping")
def foo():
    return {"status":"ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)