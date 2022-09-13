from flask import Flask, request, jsonify, render_template, url_for, redirect
from sql.sqlfunc import query
from tabulate import tabulate

wines = query('select distinct wine from viners')
winelist = [[''.join(x)] for x in wines]
years = query('select distinct years from viners')
yearlist = [[''.join(x)] for x in years]

tablewine = tabulate(winelist, tablefmt='html')
tableyear = tabulate(yearlist, tablefmt='html')

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        wine = request.form['wine']
        year = request.form['year']
        return redirect(url_for('result', wine=f'{wine} {year}'))
    else:
        return render_template('start.html') + tablewine + tableyear

@app.route('/<wine>')
def result(wine):
    return f'<h1>{wine}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
