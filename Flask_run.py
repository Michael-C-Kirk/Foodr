from flask import Flask, request, redirect, render_template
import APIcalls as api
import decode as dcd
import decision_tree as dt
import categories as c
from random import randrange
from helper import time_parse, age_paser
import restarauntURL as ru

KEY_WORD_LIST = ["sushi", "spaghetti", "taco", "ramen", "sandwich", "icecream", "kbbq", "fish", "soup", "pancake"]
clf = None
app = Flask(__name__)
details = dict()


@app.route('/thumpup')
def upbutton():
    print("AFTER UP")
    print(REST_ID)
    url = ru.getRestarauntURL(REST_ID)
    return redirect(url)
        
@app.route('/')
def index():
    clt = dt.train_initial_data()
    return render_template('index.html')
@app.route('/surprise')
def surprise():
    foodDict = api.call("7000", KEY_WORD_LIST[randrange(0, len(KEY_WORD_LIST))])
    binfo = dcd.ratingParser(foodDict, 4)[1]
    if len(binfo) == 0:
        return render_template('surprise.html', name = "All locations are closed at the moment", image = "We appologize for the inconvenience", rating = "")
    placeNum = randrange(0, len(binfo))
    REST_ID = binfo[placeNum][3]
    url = ru.getRestarauntURL(REST_ID)
    return render_template('surprise.html', name = binfo[placeNum][0], image = binfo[placeNum][2], rating = binfo[placeNum][1], URL = url)
    
@app.route('/caffeine')
def coffee():
    print("IN COFFEE!!!")
    foodDict = api.call("5000", "cafe and coffee")
    binfo = dcd.ratingParser(foodDict, 3.5)[1]
    if len(binfo) == 0:
        return render_template('caffeine.html', name = "All locations are closed at the moment", image = "We appologize for the inconvenience", rating = "")
    placeNum = randrange(0, len(binfo))
    REST_ID = binfo[placeNum][3]
    url = ru.getRestarauntURL(REST_ID)
    return render_template('caffeine.html', name = binfo[placeNum][0], image = binfo[placeNum][2], rating = binfo[placeNum][1], URL = url)
    
@app.route('/quick')
def quick():
    print("IN QUICK!!!")
    foodDict = api.call("5000", "fast food")
    binfo = dcd.ratingParser(foodDict, 3.5)[1]
    if len(binfo) == 0:
        return render_template('quick_response.html', name = "All locations are closed at the moment", image = "We appologize for the inconvenience", rating = "")
    placeNum = randrange(0, len(binfo))
    REST_ID = binfo[placeNum][3]
    url = ru.getRestarauntURL(REST_ID)
    return render_template('quick_response.html', name = binfo[placeNum][0], image = binfo[placeNum][2], rating = binfo[placeNum][1], URL = url)
    #return render_template('quick_response.html')

    
@app.route('/choose')
def choose():
    return 'results go here'

@app.route('/details_given', methods = ['POST'])
def detailed():
    if request.form['action'] == 'happy':
        print("GOT HAPPY")
        details['mood'] = 1
    elif request.form['action'] == 'sad':
        print("GOT SAD")
        details['mood'] = 0
    else:
        print("ERROR")

    if request.form['price'] == None:
        print("WHAT?")
    details['price'] = request.form['price']
    
    print(details)
    #return details
    return redirect('/choose')

if __name__ == '__main__':
    app.run()
