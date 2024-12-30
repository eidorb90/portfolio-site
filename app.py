from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_list = [
        {
            "title": "Portfolio Website",
            "description": "This is my portfolio website, no url to it because you are currently on it.",
            "technologies": ["Python","Flask", "HTML", "CSS", "JavaScript"],
            "image": "portfolio.png"
            
        },

        {
            "title": "College Football Bowl Games Predictor",
            "description": "This is a site that allows people with the code to predict who they think will win and keep track of everones picks untill the end.",
            "technologies": ["Python", "Flask", "HTML", "CSS", "JavaScript"],
            "url": "https://cfbg-cfdfd3dbe1a7.herokuapp.com/picker",
            "github": "https://github.com/eidorb90/college-football-bowl-games",
            "image": "CFBG.png"
        },

        {
            "title": "John Conways Game of Life",
            "description": "Zero player game that simulates the life of cells on a grid. This was made in Python using Pygame, but translated into JavaScript to be displayed on the web.",
            "technologies": ["Python", "Pygame"],
            "url": "/game-of-life",
            "github": "https://github.com/eidorb90/john_conways_game_of_life",
            "gif": "jcgl.gif"
        },

        {
            "title": "Kate's Fantasy",
            "description": "This is a game that I started to work on for my girlfriend. It is a 2D survival game that is still in the early stages of development.",
            "technologies": {"Godot", "GDScript"},

        }

    ]

    return render_template('projects.html', projects=projects_list)

@app.route("/services")
def services():
    return render_template('services.html')

@app.route('/game-of-life')
def game_of_life():
    return render_template('game-of-life.html')

if __name__ == '__main__':
    app.run(debug=True)