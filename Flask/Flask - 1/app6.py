from flask import Flask,request,render_template, session, make_response, flash

app=Flask(__name__, template_folder='templates')
app.secret_key = 'SOME KEY'

@app.route('/')
def index():
    return render_template('index3.html', message='Index')

@app.route('/set_data')
def set_data():
    session['name'] = 'Abhishek'
    session['other'] = 'Hello World'
    return render_template('index3.html', message='Session data set.') #Session will be stored in cookies and is not visible

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name'] 
        other = session['other']
        return render_template('index3.html', message=f'Name:{name}, Other:{other}')
    else:
        return render_template('index3.html', message='No session found')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index3.html', message='Session cleared')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index3.html', message='Cookie set.'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index3.html', message=f'Cookie Value:{cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index3.html', message='Cookie removed.'))
    response.set_cookie('cookie_name', expires=0)
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'abhishek' and password == '12345':
            flash('Successful Login')
            return render_template('index3.html', message='Login Success')
        else:
            flash('Invalid Credentials')
            return render_template('index3.html')
    return render_template('login.html')

"""
 Cookies
A cookie is a small piece of data that is stored in the user's browser.
Flask can send a cookie to the browser, and every time the user sends a request, the cookie is included.
Cookies are used for things like tracking user preferences, remembering login information, etc.

Sessions
A session is a way to store information specific to a user on the server.
Unlike cookies, session data is stored on the server, and only the session ID (a unique key) is stored in the browser as a cookie.
Flask sessions use cookies to store session data in a secure way. The session data itself is stored on the server, but the session ID is stored as a cookie in the user's browser.

Key Differences:
Cookies are stored in the user's browser and are sent back to the server with each request. They can be seen and modified by the user.
Sessions store data on the server, and only a session ID is stored in the user's browser. Sessions are more secure because the data itself isn’t exposed to the user.
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5555,  debug=True)