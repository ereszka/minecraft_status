from flask import Flask
from flask import render_template
import requests, os
from dotenv import load_dotenv


app = Flask(__name__)

@app.route("/")
def home():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    if API_KEY is None:
        return render_template('home.html', error="API key not found in environment variables.")
    r = requests.get("https://api.ngrok.com/endpoints",
                headers={"Authorization": f"Bearer {API_KEY}",
                         "Ngrok-Version": "2"})
    
    if r.status_code != 200:
        return render_template('home.html', error="Failed to fetch data from ngrok API.")
     
    return render_template('home.html', data=r.json())

if __name__ == '__main__':
   app.run(debug=True)
