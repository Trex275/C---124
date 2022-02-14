from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [{
    'id': 1, 'title': u'do homework', 'description': u'English WS 2 Annonations', 'done': False
},
    {'id': 2, 'title': u'revise physics',
        'description': u'Thermal physics', 'done': False}
]


@app.route("/")
def print():
    return jsonify({
        "data": tasks
    })


@app.route("/getdata", methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Please Provide Data"
        })
    Task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description'),
        'done': False
    }
    tasks.append(Task)
    return jsonify({
        "status": "sucsessful"
    })


if __name__ == "__main__":
    app.run(debug=True)
