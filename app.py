from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def check_email(email):
    url = f"https://api.xposedornot.com/v1/check-email/{email}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if data.get("breaches"):
                return "❌ Breach Found!"
            else:
                return "✅ Safe! No breach found"
        else:
            return "⚠️ Error checking email"

    except:
        return "Error occurred"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        email = request.form["email"]
        result = check_email(email)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)