from flask import Flask, render_template, abort

app = Flask(__name__)


projects =[
    {
        "name" : "Habit tracking app with Pyhton and MongoDB",
        "thumb" : "img/habit-tracking.png",
        "hero" : "img/habit-tracking-hero.png",
        "categories" : ["python","web"],
        "slug" : "habit-tracking",
        "prod" : "https://udemy.com",
    },
    {
        "name" : "Habit tracking app with Pyhton and MongoDB",
        "thumb" : "img/personal-finance.png",
        "hero" : "img/habit-tracking-hero.png",
        "categories" : ["react","web"],
        "slug" : "personal-finance",
        "prod" : "https://udemy.com",
    },
     {
        "name" : "Habit tracking app with Pyhton and MongoDB",
        "thumb" : "img/rest-api-docs.png",
        "hero" : "img/habit-tracking-hero.png",
        "categories" : ["writing"],
        "slug" : "api-docs",
        "prod" : "https://udemy.com",
    }
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])

if __name__ == "__main__":
    app.run(debug=True)
