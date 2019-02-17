from flask import Flask, request, redirect, render_template
import APIcalls as api
import parser as parse
from rrandom import randrange


app = Flask(__name__)
details = dict()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quick')
def quick():
    print("IN QUICK!!!")
    foodDict = api.call("5000", "fast food")
    binfo = parse.ratingParser(foodDict, 3.5)[1]
    print(binfo)
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
