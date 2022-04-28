from flask import Flask, render_template, request, redirect, session, jsonify
from werkzeug.utils import secure_filename
# from flask_login import login_required, current_user, login_user, logout_user
import os
from tools import checkfiletype as c
from tools import validate_data as v

app = Flask(__name__, template_folder='template', static_folder='uploads')

credentials = {"user": "admin", "password": "admin"}

app.secret_key = "1191"
app.config['UPLOAD_PATH'] = 'uploads'


# default page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if username == credentials["user"] and password == credentials["password"]:
            session["user"] = username
            return redirect("/dashboard")
        return "<h2> Wrong username/ password combination</h2>"
    return render_template("login.html")


# route for dashboard
@app.route('/dashboard')
def dashBoard():
    if 'user' in session and session["user"] == credentials["user"]:
        return render_template("dashboard.html")
    return "<h2> Sorry! you need to login to view the dashboard </h2>"


# route for uploading file
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        file_name = request.files["filename"]
        if file_name != " ":
            session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_PATH'], file_name.filename)
            # check file extension and data
            if c.isCSV() is True:
                file_name.save(os.path.join(app.config['UPLOAD_PATH'], secure_filename(file_name.filename)))
                return redirect('/checkdata')
            else:
                return render_template('dashboard.html', error="Not a CSV file")
        else:
            return "<h2>No file uploaded</h2>"


# route for validating csv file
@app.route('/checkdata')
def checkData():
    if v.checkCSV() == "Yes":
        return redirect("/showdata")


# route for showing options
@app.route('/showdata', methods=['GET', 'POST'])
def showData():
    return render_template("display.html")


# route for dewpoint
@app.route('/dewpoint', methods=['GET', 'POST'])
def showDewPoint():
    return render_template("dewpoint.html")


# route for appliance
@app.route('/appliance', methods=['GET', 'POST'])
def showAppliance():
    return render_template("appliance.html")


# route for light
@app.route('/lights', methods=['GET', 'POST'])
def showLights():
    return render_template("lights.html")


# route for kitchen temperature
@app.route('/temp1', methods=['GET', 'POST'])
def showKitchenTemp():
    return render_template("temp_kitchen.html")


# route for logout
@app.route('/logout')
def logout():
    session.pop("user")
    return redirect('/')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
