from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/frame', methods=['GET', 'POST'])
def frame():
    if request.method == 'POST':
        text = request.form.get('text')
        updated = request.form.get('updated')
        print("text:", text)
        print("updated:", updated)
        # process the data using Python code
        # result = int(data) * 2
        # return str(result)
    return render_template('index.html', predictedText="predicted text", image="image.jpg") # send here image

    

if __name__ == '__main__':
    app.run(debug=True)