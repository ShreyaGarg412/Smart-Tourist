from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PLACES = {
    "delhi": ["India Gate", "Red Fort", "Qutub Minar"],
    "jaipur": ["Hawa Mahal", "City Palace", "Amber Fort"],
    "agra": ["Taj Mahal", "Agra Fort"]
}

@app.route("/")
def home():
    return "Smart Tourist Backend Running ✅"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["email"] == "test@gmail.com" and data["password"] == "1234":
        return jsonify({"message": "Login Success"})
    return jsonify({"message": "Invalid Credentials"}), 401

@app.route("/places")
def places():
    city = request.args.get("city", "").lower()
    return jsonify({"places": PLACES.get(city, [])})

@app.route("/weather")
def weather():
    return jsonify({
        "temp": "28°C",
        "condition": "Sunny"
    })

@app.route("/budget")
def budget():
    amount = int(request.args.get("amount"))
    if amount < 3000:
        plan = "Low budget trip (hostel + bus)"
    elif amount < 7000:
        plan = "Medium budget trip (hotel + cab)"
    else:
        plan = "Luxury trip (resort + flight)"

    return jsonify({"plan": plan})

if __name__ == "__main__":
    app.run(debug=True)
