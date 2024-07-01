# -*- coding: utf8 -*-

"""
测试vue请求flask接口
"""

from flask import Flask, request, make_response, url_for, jsonify

from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello world."


@app.route("/getMsg", methods=['GET', 'POST'])
def getMsg():
    response = {
        "msg": "Hello, Python."
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)  # localhost:5000
