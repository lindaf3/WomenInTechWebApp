# Venus Hacks
# Authors: Yvonne Cruz, 
# 4/24/2021
# 

import requests, json
from flask import Flask, render_template, flash, redirect, request
import cv2
from backend.job_search_backend import get_input
from backend.mentors import add_mentor, search_field, search_location
#import backend.project_ideas 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hackathon'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

DIRECTORY = {}
DIRECTORY['zhiHau475'] = ['Mary Kane', 'Quality Assurance Engineer', 'America'] 
DIRECTORY['sdEddy4567'] = ['Shelly Zhang', 'Software Engineer', 'Canada'] 
DIRECTORY['julie34564'] = ['Sarah J. Smith', "Computer Engineer", 'America'] 
DIRECTORY['dann34fan'] = ['Dan O. Jones', 'Video Game Developer', 'UK'] 
DIRECTORY['maryjone443'] = ['Sarah J. Smith', 'Computer Engineer', 'France'] 
DIRECTORY['defes45667'] = ['James Capello', "Computer Engineer", 'America'] 
DIRECTORY['4833dange4'] = ['Jane T. Foster ', "Software Engineer",'Italy' ] 
DIRECTORY['dede5674'] = ['Talia Wright', 'Video Game Developer', 'America'] 
DIRECTORY['green4651123d'] = ['Mia Phan', "Video Game Developer", 'America']

   

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
        result = get_input(title,country)
        #redirect here
        return render_template('result.html', result=result)
    return render_template('jobsearch.html')

#adding and viewing mentors
@app.route('/mentors', method=('GET','POST'))
def mentors():
    if request.method == "POST":
        name = request.form.get('fullname') 
        field = request.form.get('job')
        linkedin = request.form.get('linkedin') 
        location = request.form.get('country')
        mentor = [name, field, linkedin, location]
        message = add_mentor(mentor, DIRECTORY)
        return render_template('mentors.html', message=message, m2="", m3="")

        field = request.form.get('field')
        m2 = search_field(field, DIRECTORY)
        return render_template('mentors.html', message="", m2=m2, m3="")

        location = request.form.get('location')
        m3 = search_location(l, DIRECTORY)
        return render_template('mentors.html', message="", m2="", m3=m3)
        

#posting project ideas
# @app.route('/projectideas', methods=('GET', 'POST'))
# def project():
#     return render_template('projectideas.html')

 
