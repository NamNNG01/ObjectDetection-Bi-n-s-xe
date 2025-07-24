

from flask import Flask, render_template, request
import os
from detect import detect_plate

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["image"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        detect_plate(filepath)
        return render_template("index.html", output_image="static/output.jpg")

    return render_template("index.html", output_image=None)

if __name__ == "__main__":
    app.run(debug=True)
