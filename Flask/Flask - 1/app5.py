from flask import Flask,request,render_template

app=Flask(__name__, template_folder='templates',static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5555,  debug=True)