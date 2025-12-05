from flask import Flask, redirect, request
import json

# for testing until we can use the database
FILEPATH = "./data.json"

def getUserData(filepath):
    with open(FILEPATH, "r") as file:
        return json.load(file)

def writeUserData(data, filepath):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found"


@app.route("/")
def root():
    return "Hello World"


@app.route("/read/<id>")
def read_id(id):
    userData = getUserData(FILEPATH)

    user = userData.get(id)

    if user is not None:
        return userData[id]
    else:
        return redirect("/404")


@app.route("/list")
def list_users():
    userData = getUserData(FILEPATH)

    return userData


# implementation needs improvement, no data sanitation or error checking
# will fix later
@app.route("/update/<id>", methods=["POST"])
def update_id(id):
    # get request body as json
    # gives error if Content-Type is not application/json
    requestData = request.get_json()

    userData = getUserData(FILEPATH)

    idExists = userData.get(id)

    # return error 400 if ID not present
    if idExists is None:
        return "ID not found", 400

    if "username" in requestData:
        userData[id]["username"] = requestData["username"]
    if "email" in requestData:
        userData[id]["email"] = requestData["email"]

    writeUserData(userData, FILEPATH)

    return requestData, 200

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
