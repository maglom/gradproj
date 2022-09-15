from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True
@app.route('/', methods=['GET'])
def dropdown():
    wines = ['Petrus', "Baron Philippe de Rothschild Chateau d'Armailhac","Chateau Angelus","Chateau Ausone","Chateau Batailley Grand Cru",
"Chateau Bellevue-Mondotte","Chateau Beychevelle","Chateau Branaire-Ducru","Chateau Brane-Cantenac","Chateau Calon-Segur","Chateau Canon",
"Chateau Cantemerle","Chateau Cheval Blanc","Chateau Clerc-Milon","Chateau Climens","Chateau Clinet","Chateau Cos d'Estournel","Chateau Cos d'Estournel Blanc",
"Chateau d'Yquem","Chateau de Fargues","Chateau Doisy-Vedrines","Chateau Ducru-Beaucaillou","Chateau Duhart-Milon","Chateau Faugeres","Chateau Figeac",
"Chateau Giscours","Chateau Giscours La Sirene de Giscours","Chateau Grand-Puy-Lacoste","Chateau Gruaud-Larose","Chateau Gruaud-Larose 'Sarget de Gruaud-Larose'",
"Chateau Haut-Bailly","Chateau Haut-Batailley","Chateau Haut-Brion","Chateau L'Eglise-Clinet","Chateau La Conseillante","Chateau La Fleur-Petrus",
"Chateau La Mission Haut-Brion","Chateau Lafite Rothschild","Chateau Lafite Rothschild 'Carruades de Lafite'","Chateau Lafleur","Chateau Lagrange","Chateau Lascombes",
"Chateau Latour","Chateau Latour-Martillac","Chateau Latour 'Les Forts de Latour'","Chateau Leoville-Las Cases 'Clos du Marquis'","Chateau Leoville-Las Cases 'Grand Vin de Leoville'",
"Chateau Leoville Barton","Chateau Leoville Poyferre","Chateau Lynch-Bages","Chateau Margaux","Chateau Montrose","Chateau Mouton Rothschild","Chateau Nenin","Chateau Palmer",
"Chateau Pape Clement","Chateau Pavie","Chateau Pichon-Longueville au Baron de Pichon-Longueville","Chateau Pichon Longueville Comtesse de Lalande","Chateau Pontet-Canet",
"Chateau Rauzan-Segla","Chateau Smith Haut Lafitte","Chateau Suduiraut","Chateau Talbot","Chateau Troplong Mondot","Chateau Trotanoy","Chateau Trotte Vieille",
"Denis Dubourdieu Chateau Doisy-Daene L'Extravagant de Doisy-Daene","Domaine de Chevalier","Donjon de Lamarque","La Clarte de Haut-Brion Blanc","Le Clarence de Haut-Brion - Chateau Bahans Haut-Brion",
"Le Pin","Pavillon Blanc du Chateau Margaux","Pavillon Rouge du Chateau Margaux","vieux Chateau Certan"
]
    years = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022"]
    return render_template('wine2.html', wines=wines, years=years)
if __name__ == "__main__":
    app.run(debug=True)

   