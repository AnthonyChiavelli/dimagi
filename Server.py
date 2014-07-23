from __future__ import print_function
import json
import datetime
from flask import Flask
from flask import request
import LocationQuerier
from main import output_data

app = Flask(__name__)

@app.route("/checkin", methods=['POST'])
def check_in():
    """
    API endpoint for sending POST requests to check in to a location
    """
    try:
        phone_number = request.form['phone_number']
        location = request.form['location']
    except KeyError:
        return "Invalid parameters!"


    # Make API query with location name
    lat, lng = LocationQuerier.query_location(location)

    # Encode user info and location result into JSON
    time_stamp = datetime.datetime.utcnow()
    output_data(phone_number, str(time_stamp), (lat, lng))

    return "Parameters Processed"

app.run()