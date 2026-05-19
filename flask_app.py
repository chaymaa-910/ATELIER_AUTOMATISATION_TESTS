from flask import Flask, render_template
import requests
import time
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def consignes():
    return render_template("consignes.html")


@app.route("/monitoring")
def monitoring():

    url = "https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&current=temperature_2m"

    start = time.time()

    try:

        response = requests.get(url)

        response_time = round((time.time() - start) * 1000, 2)

        if response.status_code == 200:

            data = response.json()

            temperature = data["current"]["temperature_2m"]

            status = "✅ API opérationnelle"

        else:

            temperature = "Erreur"

            status = "❌ API indisponible"

    except Exception:

        response_time = "Erreur"

        temperature = "Erreur"

        status = "❌ Impossible de contacter l'API"

    return render_template(
        "monitoring.html",
        status=status,
        response_time=response_time,
        temperature=temperature,
        date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
