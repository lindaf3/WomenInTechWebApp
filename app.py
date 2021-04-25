# Venus Hacks
# Authors: Yvonne Cruz, 
# 4/24/2021
# 

import requests, json
from flask import Flask, render_template, flash, redirect, request, url_for
import cv2
from backend.job_search_backend import get_input
from backend.mentors import add_mentor, search_field, search_location
from backend.project_ideas import add_project_idea, up_vote, down_vote 


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

chrp = []
p = add_project_idea(chrp, "Build a website about your favorite TV series", "Bob Billy")
p = add_project_idea(chrp, "Build an android app based on a simple to-do list", "Bill Bobby")
p = add_project_idea(chrp, "Build a website about your favorite TV series", "Kaela Kealoha")
p = add_project_idea(chrp, "Build a website with the Spotify API", "Kiana Kealoha")
p = add_project_idea(chrp, "Build yourself a weather app!", "Sabrina Capello")
p = add_project_idea(chrp, "Create a website to teach people about sustainability", "Chanda Misra")
p = add_project_idea(chrp, "Make a video game!", "Billy Bob")
p = add_project_idea(chrp, "Make a health app to stay fit!","Reckless Man")
p = add_project_idea(chrp,"Location tracker for when you lose your friends","Turtle Boy")
p = add_project_idea(chrp,"Build yourself a virtual paint wheel for color mixing","Chalk Prince")
p = add_project_idea(chrp,"Build an app to help you invest money and get rich","Eclipse Star")

   

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
@app.route('/connect', methods=('GET', 'POST'))
def connect():
    return render_template('connect.html', message="", m2="", m3="")

@app.route('/connect1', methods=('GET','POST'))
def connect1():
    if request.method == "POST":
        name = request.form.get('fullname') 
        field = request.form.get('job')
        linkedin = request.form.get('linkedin') 
        location = request.form.get('country')
        mentor = [name, field, linkedin, location]
        message = add_mentor(mentor, DIRECTORY)
        return render_template('connect.html', message=message, m2="", m3="")
    return render_template('connect.html', message="", m2="", m3="")

@app.route('/connect2', methods=('GET','POST'))
def connect2():
    if request.method == "POST":
        field = request.form.get('field')
        m2 = search_field(field, DIRECTORY)
        return render_template('connect.html', message="", m2=m2, m3="")
    return render_template('connect.html', message="", m2="", m3="")
        
@app.route('/connect3', methods=('GET','POST'))
def connect3():
    if request.method == "POST":
        location = request.form.get('location')
        m3 = search_location(location, DIRECTORY)
        return render_template('connect.html', message="", m2="", m3=m3)
    return render_template('connect.html', message="", m2="", m3="")

#posting project ideas
@app.route('/project', methods=('GET', 'POST'))
def project():
    if request.method == "POST":
        name = request.form.get('name')
        ideas = request.form.get('ideas')
        posts = add_project_idea(chrp,ideas,name)
        return render_template('project.html', posts=posts)
    return render_template('project.html', posts="")

@app.route('/pro1', methods=('GET', 'POST'))
def pro1():
    return render_template('/projects/pro1.html')

@app.route('/pro2', methods=('GET', 'POST'))
def pro2():
    return render_template('/projects/pro2.html')

@app.route('/pro3', methods=('GET', 'POST'))
def pro3():
    return render_template('/projects/pro3.html')

@app.route('/pro4', methods=('GET', 'POST'))
def pro4():
    return render_template('/projects/pro4.html')

@app.route('/pro5', methods=('GET', 'POST'))
def pro5():
    return render_template('/projects/pro5.html')

@app.route('/pro6', methods=('GET', 'POST'))
def pro6():
    return render_template('/projects/pro6.html')

@app.route('/pro7', methods=('GET', 'POST'))
def pro7():
     return render_template('/projects/pro7.html')




 
