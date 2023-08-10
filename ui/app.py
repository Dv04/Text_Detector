from flask import Flask, render_template, request, url_for, session
import os
import secrets
from datetime import datetime

# Generate a secure random secret key
secret_key = secrets.token_hex(16)  # 16 bytes (128 bits) key

app = Flask(__name__)
app.secret_key = secret_key


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/frame", methods=["GET", "POST"])
def frame():
    if "image_index" not in session:
        session["image_index"] = 1

    image_index = session["image_index"]
    image_filename = f"{image_index:03d}.jpg"
    image_url = url_for("static", filename=f"image/{image_filename}")
    print(image_filename, image_index, image_url)

    if request.method == "POST":
        text = request.form.get("text")
        updated = request.form.get("updated")
        print("text:", text)
        print("updated:", updated)
        # process the data using Python code
        # result = int(data) * 2
        # return str(result)

        # Update image index for the next image
        session["image_index"] = (image_index + 1) % 161  # Assuming 160 images
        # After the session is updated
        print("Session image index:", session["image_index"])

    # Add this print statement
    print("Image index:", image_url)
    return render_template(
        "index.html",
        predictedText="predicted text",
        Image=image_url,
        current_time=datetime.now().timestamp(),
    )


if __name__ == "__main__":
    app.run(debug=True)
