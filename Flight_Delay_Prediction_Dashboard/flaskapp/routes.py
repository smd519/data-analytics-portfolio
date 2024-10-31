""" routes.py - Flask route definitions

Flask requires routes to be defined to know what data to provide for a given
URL. The routes provided are relative to the base hostname of the website, and
must begin with a slash."""
from flaskapp import app
from flask import render_template, request, jsonify

import pickle
import pandas as pd
import numpy as np
import json


# The following two lines define two routes for the Flask app, one for just
# '/', which is the default route for a host, and one for '/index', which is
# a common name for the main page of a site.
#
# Both of these routes provide the exact same data - that is, whatever is
# produced by calling `index()` below.


@app.route('/')
@app.route('/index')
def index():
    """Renders the index.html template"""
    # Renders the template (see the index.html template file for details). The
    # additional defines at the end (table, header, username) are the variables
    # handed to Jinja while it is processing the template.
    return render_template('index.html')


@app.route('/get_results', methods=['POST'])
def get_results():
    month = request.json['month']
    dayOfWeek = request.json['dayOfWeek']
    year = request.json['year']
    season = request.json['season']
    departureTimeFeature = request.json['departureTimeFeature']
    airlineCodesFeature = request.json['airlineCodesFeature']
    originCodeFeature = request.json['originCodeFeature']
    destCodeFeature = request.json['destCodeFeature']
    distanceFeature = request.json['distanceFeature']

    synthetic_data = pd.DataFrame({'Month': month,
                                   'DayOfWeek': dayOfWeek,
                                   'Year': year,
                                   'Season': season,
                                   'Sched_dep_time': departureTimeFeature,
                                   'Airline_code': airlineCodesFeature,
                                   'Origin_code': originCodeFeature,
                                   'Dest_code': destCodeFeature,
                                   'Distance': distanceFeature})

    results = pred_prob(synthetic_data)

    predictions = []
    for index, row in results.iterrows():
        prediction = {}
        prediction['airlineCode'] = index
        prediction['low'] = row['low']
        prediction['medium'] = row['medium']
        prediction['high'] = row['high']
        predictions.append(prediction)

    final_results = {'results': predictions}
    print(final_results)
    return (json.dumps(final_results))


def pred_prob(data):
    filename1 = './flaskapp/model/first_stage_model.sav'
    model_1 = pickle.load(open(filename1, 'rb'))
    filename2 = './flaskapp/model/second_stage_model.sav'
    model_2 = pickle.load(open(filename2, 'rb'))
    prob_1 = model_1.predict_proba(data)
    # prob_low_delay = prob_1[:, 0]
    prob_2 = model_2.predict_proba(data)
    prob_non_low = np.tile(prob_1[:, 1], (2, 1)).transpose()
    prob_med_high = np.multiply(prob_non_low, prob_2)
    final_probs = np.hstack((prob_1[:, 0][:, np.newaxis], prob_med_high))
    return pd.DataFrame(final_probs, columns=['low', 'medium', 'high'], index=data['Airline_code'])
