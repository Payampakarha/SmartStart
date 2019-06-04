# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
import pandas as pd


# Create the application object
app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def home_page():
    return render_template('index.html')  # render a template

@app.route('/output',methods=["GET","POST"])
def tag_output():
#
       # Pull input
       city = request.form.get('city')
       business_type =request.form.get('business')
       slider_value = int(request.form.get('slider'))
       #read result file
       results_filename = './data/' + business_type + '_in_' + city + '_results.csv'
       df = pd.read_csv(results_filename)
       shorten_df = df.sort_values('PS', ascending =True)[slider_value:slider_value+5]
       points = shorten_df.to_dict('records')

       #Create the string that would load the map according to the input 
       map_folder = '../static/maps'
       map_filename = map_folder + '/map_' + business_type + '_in_' + city + '_' + str(slider_value) + '_' + str(slider_value+5) + '.html'
       print (map_filename)
       return render_template("index.html", points=points, map_filename = map_filename)

# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True) #will run locally http://127.0.0.1:5000/

