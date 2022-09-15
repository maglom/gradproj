from flask import Flask, flash, redirect, render_template, \
request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        data = [{"name":'Petrus'}, {"name":"Baron Philippe de Rothschild Chateau d'Armailhac"},{"name":"Chateau Angelus"}],
        data2 = [{"name":"2001"},{"name":"2002"}, {"name":"2003"}
])

@app.route("/test", methods = ['GET', 'POST'])


def test():
    select1 = request.form.get('comp_select_y')
    select2 = request.form.get('comp_select')
    return {"Vintage": select1, "Wine": select2}
        
    

if __name__ == '__main__':
   app.run(debug = True)