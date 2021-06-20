from flask import Flask, render_template, redirect, make_response, send_file
from main import create_sheet
from dummy_data import data

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html', data=data)


@app.route('/myfile')
def myfile():
    response = make_response(create_sheet())
    response.headers["Content-Disposition"] = "attachment; filename=" + \
                                        "sheet.xlsx"
    response.headers["Content-type"] = \
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    return response

