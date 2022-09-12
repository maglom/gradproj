from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('start.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
