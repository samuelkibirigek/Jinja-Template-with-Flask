from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    my_name = "Kibirige Kalule Samuel"
    return render_template("index.html", num=random_number, year=current_year, name=my_name)


@app.route("/guess/<your_name>")
def game(your_name):

    # get data on gender from API and place it in variable
    gender_url = f"https://api.genderize.io/?name={your_name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    the_gender = gender_data["gender"]

    # get data from API on age and place it in variable
    age_url = f"https://api.agify.io/?name={your_name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    the_age = age_data["age"]

    the_name = your_name.title()

    return render_template("about.html", name=the_name, gender=the_gender, age=the_age)


if __name__ == "__main__":
    app.run(debug=True)


