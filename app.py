import os
import time

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
import csv
from helper import CheggHelper

config = dotenv_values(".env")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gtkcs_members.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
session = db.session
db.create_all()


def Load_Data(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        return [d for d in csv_reader]


class User(db.Model):
    __tablename__ = config["TABLENAME"]
    username = db.Column(db.String, primary_key=True, nullable=False)
    passcode = db.Column(db.String)


@app.route('/init_table')
def initTable():
    try:
        file_name = config["CSV_FILE"]
        data = Load_Data(file_name)
        for i in data:
            record = User(**{
                'username': i[0],
                'passcode': config["PASSCODE"]
            })
            session.add(record)
        session.commit()
    except Exception as e:
        print("ERROR:", e)
        session.rollback()
        return e
    finally:
        session.close()
    return "Successfully Initialized Table"


@app.route('/chegg')
def openChegg():
    link = request.args.get("link")
    if not link:
        resp = jsonify("Question Link Missing")
        resp.status_code = 500
        return resp
    obj = CheggHelper()
    success, answer, description = obj.getQAns(link)
    if success:
        print("Success...")
    else:
        print("ERROR")
    return render_template("answer.html", snippet=answer)


if __name__ == '__main__':
    app.run(debug=True)
