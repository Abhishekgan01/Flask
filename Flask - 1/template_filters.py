
from flask import Flask,request,render_template, redirect, url_for

app=Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    mylist = [10,20,30,40,50]
    return render_template('index.html',mylist=mylist)

@app.route('/other')
def other():
    some_text = "Hello World"
    return render_template('other.html',some_text=some_text)

#Customer Filters
@app.template_filter('reverse_string') #Custom Filter called in other.html
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat') #Custom Filter called in other.html
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case') #Custom Filter called in other.html
def alternate_case(s):
    return ''.join([c.upper() if i%2 == 0 else c.lower() for i,c in enumerate(s)])

@app.route('/redirect')
def others():
    some_text = "Hello World"
    return render_template('other.html',some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('others')) #directly redirecting to other html page using endpoint

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5555,  debug=True)
