from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from imdb_crawler import *
from get_movies import *
from label import *
from score import *
import requests
import json
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
'''
@app.route("/", methods=['GET', 'POST'])
def hello():
    render_template("hello.html")
    form = ReusableForm(request.form)
    x = []
    if request.method == 'POST':
        name = request.form['name']
        # json = JSON.parse(request.body)
        # json["review"]
        print(name)

        if form.validate():
            name = str(name)
            if name[0] is '1':
                # name = city name
                x = movie_list(name)
                print(x)
                return jsonify(
                  results = x
                )
            elif name[0] is '2':
                # name = movie title
                x = getuser_review(name)
                print(x)
                return jsonify(
                    results=x
                )
            else:
                # name = full review
                x = get_score(name)
                print(x)
                y = get_label(name)
                print(y)
                return jsonify(
                    score=x,
                    label=y
                )

        #else:
            # flash('All the form fields are required. ')
            # requests.post('MINERVA_URL', data = {'score':'value', 'label' :'value'})
'''
@app.route("/list", methods=['POST'])
def list():

    x = []
    if request.method == 'POST':
        name = json.loads(request.data)['city']
        print(name)

        if name != None and name !="":
            name = str(name)
            # name = city name
            x = movie_list(name)
            print(x)
            return jsonify(
              results = x
            )
        else:
            return jsonify(
              results = "Error: Please send city name"
            )

@app.route("/review", methods=['POST'])
def review():

    x = []
    if request.method == 'POST':
        name = json.loads(request.data)['movie']
        print(name)

        if name != None and name !="":
            name = str(name)
            x = getuser_review(name)
            print(x)
            return jsonify(
              results = x
            )
        else:
            return jsonify(
              results = "Error: Please send movie title"
            )

@app.route("/sentiment", methods=['POST'])
def sentiment():

    x = []
    if request.method == 'POST':
        name = json.loads(request.data)['review']
        # print(name)

        if name != None and name !="":
            # name = full review
            x = get_score(name)
            print(x)
            y = get_label(name)
            print(y)
            return jsonify(
                score=x,
                label=y
            )
        else:
            return jsonify(
              results = "Error: Please send movie review string."
            )

if __name__ == "__main__":
    app.run()
