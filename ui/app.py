from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__, static_url_path="/static")

img = os.path.join("image")
file = os.path.join(img, "001.jpg")
print(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/frame", methods=["GET", "POST"])
def frame():
    image_url = url_for("static", filename="image/020.jpg")  # Dynamic image URL
    if request.method == "POST":
        text = request.form.get("text")
        updated = request.form.get("updated")
        print("text:", text)
        print("updated:", updated)
        # process the data using Python code
        # result = int(data) * 2
        # return str(result)

    return render_template(
        "index.html", predictedText="predicted text", Image=image_url
    )


if __name__ == "__main__":
    app.run(debug=True)
