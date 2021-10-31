from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route('/')
def get_beer():
    
    r = requests.get("https://api.punkapi.com/v2/beers/random")
    beer = r.json()

    beer = {
            'id' : beer[0]['id'],
            'name': beer[0]['name'],
            
            'desc': beer[0]['description'],
            'foodpair': beer[0]['food_pairing'][0],
            'brewers_tips': beer[0]['brewers_tips'],

            'ingredients': beer[0]['ingredients'].keys(),
            'ph' : beer[0]['ph'],
            'alchohol_pc': beer[0]['abv']

            }

    # print(beer.items())
    
    
    return render_template('index.html', beer = beer)


if __name__=="__main__":
    app.run(debug=True)
    # get_beer()