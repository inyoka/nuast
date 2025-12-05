from flask import Flask, redirect
import json

# for testing until we can use the database
FILEPATH = "./data.json"

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found"

@app.route("/")
def root():
    return "Hello World"

@app.route("/read/<id>")
def read_id(id):
    with open(FILEPATH, "r") as file:
        userData = json.load(file)

    user = userData.get(id)

    if user is not None:
        return userData[id]
    else:
        return redirect("/404")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
