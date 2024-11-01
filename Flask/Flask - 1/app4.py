import pandas as pd
from flask import Flask,request,render_template, redirect, url_for, Response

app=Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form.get('password')
        
        if username == 'abhishek' and password == '12345':
            return "success"
        else:
            return "failure"
    

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'applications/vnd.openxmlformats-officedocument.spreadsheet.sheet' or file.content_type ==' application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
    
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)
    
    response = Response(
        df.to_csv(),
        mimetype = 'text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        } 
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5555,  debug=True)