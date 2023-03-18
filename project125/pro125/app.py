#Capital F Flask is a class
from flask import Flask, jsonify, request

from classifier import  get_prediction

app=Flask(__name__)

tasks = [
    {
        'Contact': "9987644456",
        'Name': "Raju",
        'done': 'false',
        'id':1

    },
    {
        'Contact': "9876543222",
        'Name': "Rahul",
        'done': 'false',
        'id':2
    }
]

#now define a route for the app

@app.route("/")


    
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })

if(__name__=='__main__'):
    app.run(debug=True)



