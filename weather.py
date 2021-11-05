import json
from re import split
from flask import Flask, render_template, url_for, request, redirect
from apiparsing import parsing 
                                         
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form.get('submitbutton') == 'Get Weather':
            city = request.form.get('city')
            state = request.form.get('state')
            parsing(city, state)
            return redirect(url_for('result'))                    #retrieves user input for city and state and feeds data as parameters in the 'parsing' function found in apiparsing.py - redirects to result endpoint 
    else:
        return render_template('index.html')


@app.route("/result", methods=["POST", "GET"])
def result():
    weather_day = []
    temp = []
    detailforcst = []
    icon = []                                                #storage for individual asects of the forecast 
    for day in parsing.fore:
        weather_day.append(day)
        temp.append(parsing.fore[day][0])
        detailforcst.append(parsing.fore[day][6])
        icon.append(parsing.fore[day][4])                     #appends each particular forecast aspect to storage for each time of day/day
    return render_template('results.html', days = weather_day, temp = temp, forecast = detailforcst, icon = icon)         #renders page and storage variables(for later access in the results.html)



if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)


