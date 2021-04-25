# Venus Hacks
# Authors: Yvonne Cruz, 
# 4/24/2021
# 

import requests, json
from flask import Flask, render_template, flash, redirect, request
import cv2
import backend.job_search_backend
#import backend.mentors
#import backend.project_ideas 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hackathon'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

   

#home
@app.route('/')
def index():
    return render_template('landingpage.html')


#job search
@app.route('/jobsearch', methods=('GET', 'POST'))
def jobsearch():
    if request.method == 'POST':
        #access data in POST form
        title = request.form.get('title') 
        country = request.form.get('country')
        #get_data(form.search_terms.data)
        #redirect here
        return render_template('result.html', result= title)
    return render_template('jobsearch.html')

#display results 
# @app.route('/results', methods=('GET','POST'))
# def results():
#     return render_template('results.html')

#adding and viewing mentors
# @app.route('/mentors', method=('GET','POST'))
# def mentors():
#     if request.method == "POST":
        # name = request.form.get('fullname') 
        # field = request.form.get('job')
        # linkedin = request.form.get('linkedin') 
        # location = request.form.get('country')
        # mentor = [name, field, linkedin, location]
        # message = add_mentor(mentor, DIRECTORY)
        # return render_template('mentors.html', message=message, m2="", m3="")

        # field = request.form.get('field')
        # m2 = search_field(field, DIRECTORY)
        # return render_template('mentors.html', message="", m2=m2, m3="")

        # location = request.form.get('location')
        # m3 = search_location(l, DIRECTORY)
        # return render_template('mentors.html', message="", m2="", m3=m3)
        

#posting project ideas
# @app.route('/projectideas', methods=('GET', 'POST'))
# def project():
#     return render_template('projectideas.html')

 
