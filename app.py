# Venus Hacks
# Authors: Yvonne Cruz, 
# 4/24/2021
# 

import requests, json
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import cv2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hackathon'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
bootstrap = Bootstrap(app)

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'superhero'

class Search(FlaskForm):
    search_terms = StringField('Search Terms', validators=[DataRequired()])

def get_data(data: str, indicator: int):
    key = data
    page = indicator
    #Constant required parameters
    base_url = "https://job-search4.p.rapidapi.com/indeed/"
    required = {    'x-rapidapi-key': "883f54a2eemshc4d6fd4695f96aap1cf784jsn76c6b3c90387",
                    'x-rapidapi-host': "job-search4.p.rapidapi.com"}
    try:          
        search_parameters = [('query', key), ('page', page)]
        feedback = requests.request("GET", base_url, headers=required, params=search_parameters)
        
        result = feedback.json()

        with open('jobresults.json', 'w') as json_file:
            json.dump(result, json_file)
        
    #If we recieve a JSONDecodeError, our user must have inputed the wrong stock symbol
    except json.decoder.JSONDecodeError:
        #Inform the User that we cannot find stock data for their given symbol
        print(f'Cannot find jobs for {data} on page {page}.')
            
    if __name__ == '__main__':
        get_data("qa", 1)     

#home
@app.route('/')
def index():
    return render_template('landingpage.html')

#job search
@app.route('/jobsearch', methods=('GET', 'POST'))
def jobsearch():
    if request.method == 'POST':
        title = request.form.get('title')  # access the data inside 
        country = request.form.get('country')
        #get_data(form.search_terms.data)
        #redirect here
        return render_template('landingpage.html')
    return render_template('jobsearch.html')

#results 
@app.route('/results', methods=('GET','POST'))
def results():
    return render_template('results.html')

 
