
from flask import Flask,request,make_response

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "You made a GET request\n"
    elif request.method == 'POST':
        return "You made a POST request\n"
    else:
        return "You will never see this message"
    return "Hello!"

@app.route('/hello')
def hello():
    response = make_response('Hellooo')  #response return 
    response.status_code = 202
    response.headers['content-type'] = 'text/file'
    return response

@app.route('/greet/<name>') #dynamic variable
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2 }"

@app.route('/handle_url_params') #Request Instances
def handle_params():
    #return str(request.args) - ImmutableMultiDict([])
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f"{greeting}, {name}!"
    else:
        return "Missing required parameters"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5555,  debug=True)
