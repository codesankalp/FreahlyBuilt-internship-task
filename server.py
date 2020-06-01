from flask import Flask, render_template, request, redirect
import csv
import csv_to_html
import subprocess

app = Flask(__name__)

print(__name__)
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def any_page(page_name):
    return render_template('index.html')

def write_to_csv(data):
    with open('db.csv',mode="a") as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db,delimiter=',')
        csv_writer.writerow([email,subject,message])
    subprocess.run(["python" ,"csv_to_html.py", "db.csv" ,"contact.html"])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(type(data))
        write_to_csv(data)
        return render_template('thanks.html')
    else:
        return 'something went wrong'