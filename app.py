import requests
import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    query = "London,UK"
    unit = "metric"
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    api_url = os.getenv("OPENWEATHERMAP_API_URL")
    url = "{0}/weather?q={1}&units={2}&appid={3}".format(api_url, query, unit, api_key)
    data = requests.get(url=url)

    return render_template("index.html", data=data.json())


if __name__ == '__main__':
    app.run()
