from flask import Flask, request, redirect, render_template
import APIcalls as api
import decode as dcd
from random import randrange

KEY_WORD_LIST = ["sushi", "spaghetti", "taco", "ramen", "sandwich", "icecream", "kbbq", "fish", "soup", "pancake"]

app = Flask(__name__)
details = dict()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/surprise')
def surprise():
    foodDict = api.call("7000", KEY_WORD_LIST[randrange(0, len(KEY_WORD_LIST))])
    binfo = dcd.ratingParser(foodDict, 4)[1]
    placeNum = randrange(0, len(binfo))
    return render_template('surprise.html', name = binfo[placeNum][0], image = binfo[placeNum][2], rating = binfo[placeNum][1])
    
@app.route('/caffeine')
def coffee():
    print("IN COFFEE!!!")
    foodDict = api.call("5000", "cafe and coffee")
    binfo = dcd.ratingParser(foodDict, 3.5)[1]
    placeNum = randrange(0, len(binfo))
    return render_template('caffeine.html', name = binfo[placeNum][0], image = binfo[placeNum][2], rating = binfo[placeNum][1])

@app.route('/quick')
def quick():
    print("IN QUICK!!!")
    foodDict = api.call("5000", "fast food")
    binfo = dcd.ratingParser(foodDict, 3.5)[1]
    placeNum = randrange(0, len(binfo))
    return render_template('quick_response.html', name = binfo[placeNum][0], image = binfo[placeNum][2], rating = binfo[placeNum][1])
    #return render_template('quick_response.html')

    
@app.route('/choose')
def choose():
    return 'results go here'

@app.route('/details_given', methods = ['GET'])
def detailed():
    details['price'] = request.form['price']
    details['foodtype'] = request.form['cuisine']

    print(details)
    #return details
    return redirect('/choose')

if __name__ == '__main__':
    app.run()
