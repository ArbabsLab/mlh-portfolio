import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Armando Mac Beath", title2="Fiona", url=os.getenv("URL"))

# Hobbies route which returns the hobbies html page
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Our Hobbies", url=os.getenv("URL"))

#Route for work experience page
@app.route('/work')
def work():
    return render_template('workExperience.html', title="Work Experience", url=os.getenv("URL"))

# About us route which returns the about us html page
@app.route('/about')
def about():
    return render_template('aboutUs.html', title="About Us", url=os.getenv("URL"))

#Route for education page
@app.route('/education')
def education():
    # Create a dictionary with education data for each person
    education_data = {
        "Fiona": [
            {
                "degree": "Primary School Diploma",
                "institution": "Andes International School",
                "dates": "2010 - 2016",
                "description": "School with an international curriculum.",
                "icon": "fas fa-school"
            },
            {
                "degree": "Middle School Diploma",
                "institution": "Andes International School",
                "dates": "2016 - 2019",
                "description": "Graduated with honors. ",
                "icon": "fas fa-school"
            },
        ],
        "Armando": [
            {
                "degree": "Primary School Diploma",
                "institution": "Andes International School",
                "dates": "2010 - 2016",
                "description": "School with an international curriculum.",
                "icon": "fas fa-school"
            },
            {
                "degree": "Middle School Diploma",
                "institution": "Andes International School",
                "dates": "2016 - 2019",
                "description": "Graduated with honors. ",
                "icon": "fas fa-school"
            },
            {
                "degree": "High School Diploma",
                "institution": "Prepa Tec Campus Puebla",
                "dates": "2018 - 2021",
                "description": "Program of international baccalaureate.",
                "icon": "fas fa-school"
            },
            {
                "degree": "B.S. in Mechatronics Engineering",
                "institution": "Tecnológico de Monterrey, Campus Puebla",
                "dates": "2021 - 2025",
                "description": "Specializing in automation and robotics. Lead programmer for the FRC team.",
                "icon": "fas fa-graduation-cap"
            }
        ]
    }
    # Render the education template with the education data
    return render_template('education.html', education_data=education_data)

# map route which returns the map html page
@app.route('/map')
def map():
    return render_template('map.html', title="Places we've been", url=os.getenv("URL"))

