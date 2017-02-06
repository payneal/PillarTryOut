from app.application import app
from flask import jsonify, request, Response
USERS = {}


@app.route("/user/<username>", methods=['GET'])
def access_users(username):
    if request.method == "GET":
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)
    elif request.method == "POST":
        USERS.update
