from flask import Flask, flash, redirect, render_template, request, url_for, redirect
from sql.sqlfunc import query


wines = query('select distinct wine from viners order by wine asc')
years = query('select distinct years from viners order by years asc')

winelist = [''.join(x) for x in wines]
yearlist = [''.join(x) for x in years]

winedict = [{'name':x} for x in winelist]
yeardict = [{'name':x} for x in yearlist]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index2.html', 
        data = winedict,
        data2 = yeardict)

@app.route("/test", methods = ['GET', 'POST'])


def test():
    select1 = request.form.get('comp_select_y')
    select2 = request.form.get('comp_select')
    predictions = query(f"select predictions from vin where name = '{select2}' and year = '{select1}'")
    predictions = predictions[0][0]
    rating = query(f"select rating from vin where name = '{select2}' and year = '{select1}'")
    rating = rating[0][0]
    return f"<H1>Wine = {select2}<br> Vintage = {select1}<br> Rating = {rating}<br> Predictions = {predictions}</H1>"
        
    

if __name__ == '__main__':
   app.run(debug = True)