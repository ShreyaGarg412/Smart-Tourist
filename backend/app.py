from flask import Flask, render_template, request , redirect, url_for
import requests
import os
app = Flask(__name__, template_folder="../templates", static_folder="../static")

GOOGLE_KEY = "PASTE_YOUR_GOOGLE_API_KEY"
WEATHER_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/explore/<category>", methods=["GET", "POST"])
def explore(category):
    places = []

    if request.method == "POST":
        city = request.form["city"]

        query_map = {
            "tourist": "tourist attractions",
            "restaurants": "restaurants",
            "hotels": "hotels"
        }

        query = f"{query_map[category]} in {city}"

        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {"query": query, "key": GOOGLE_KEY}
        res = requests.get(url, params=params).json()
        places = res.get("results", [])

    return render_template("explore.html", places=places, category=category)


@app.route("/weather", methods=["GET", "POST"])
def weather():
    data = None
    if request.method == "POST":
        city = request.form["city"]
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": WEATHER_KEY,
            "units": "metric"
        }
        data = requests.get(url, params=params).json()

    return render_template("weather.html", weather=data)

@app.route("/send_sos", methods=["POST"])
def send_sos():
    lat = request.form.get("lat")
    lng = request.form.get("lng")
    phone = request.form.get("phone")

    if not lat or not lng or not phone:
        return "Location or contact missing", 400

    location_link = f"https://maps.google.com/?q={lat},{lng}"
    message = f"I am in danger! My location: {location_link}"

    whatsapp_url = f"https://wa.me/{phone}?text={message}"

    return redirect(whatsapp_url)

@app.route("/safety")
def safety():
    return render_template("safety.html")

if __name__ == "__main__":
    app.run(debug=True)
