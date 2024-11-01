from flask import Flask,request,render_template

app=Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = "Learning"
    myresult = 10+20
    mylist = [10,20,30,40,50]
    return render_template('index.html',mylist=mylist)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5555,  debug=True)
    