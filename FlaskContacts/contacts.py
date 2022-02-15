from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
            {
                'ID': 1,
                'Name': 'Rishi',
                'Contact': '9987644456',
                'Done': False
            },
            {
                'ID': 2,
                'Name': 'Samuel',
                'Contact': '9876543222',
                'Done': False
            }
        ]
@app.route('/add-data',methods = ['POST'])
def addtask():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide data in json format'
        })
    task = {
        'ID':tasks[-1]['ID']+1, 
        'Title':request.json['Title'],
        'Description':request.json.get('description',''),
        'Done': False
    }
    tasks.append(task)
    return jsonify({
        'Status':SUCCESS,
        'Message': 'task added succesfully'
    })

@app.route("/get-data")
def getdata():
    return jsonify({
        'Data':tasks
    })
if (__name__ == '__main__'):
    app.run(debug = True)