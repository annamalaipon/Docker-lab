import os
from flask import Flask, render_template, abort, url_for, json, jsonify

app = Flask(__name__,template_folder='.')

color = os.environ.get("COLOR")

@app.route("/")
def index():
    return render_template('index.html', value=color)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
