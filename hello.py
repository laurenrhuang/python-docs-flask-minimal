from flask import Flask
from flask import json, request, jsonify

myapp = Flask(__name__)
app.config["DEBUG"] = True


@myapp.route("/api/upperCaseService/")
def upperCaseService():
    words_dict = dict(request.get_json())
    new_words_dict = {}
    for key, value in words_dict.items():
        new_words_dict[key] = [name.capitalize() for name in value]
    return jsonify(new_words_dict)


myapp.run()
