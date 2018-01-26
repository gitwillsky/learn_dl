import json
from flask import Flask
from flask import request 



app = Flask(__name__)

@app.route('/', methods = ['POST'])
def reg():
    dict = json.loads(request.get_data())
    a = [1, 2, 3, 4]
    return json.dumps(a)

if __name__ == '__main__':
    app.run(debug=False)