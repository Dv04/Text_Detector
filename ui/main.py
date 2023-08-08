from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)