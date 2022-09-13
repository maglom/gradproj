from flask import Flask, request, jsonify, render_template, url_for, redirect
from sql.sqlfunc import query
from tabulate import tabulate

wines = query('select wine, years from viners')
winelist = [[''.join(x)] for x in wines]

table = tabulate(winelist, tablefmt='html')

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        wine = request.form['wine']
        year = request.form['year']
        return redirect(url_for('result', wine=f'{wine} {year}'))
    else:
        return render_template('start.html') + table

@app.route('/<wine>')
def result(wine):
    return f'<h1>{wine}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
