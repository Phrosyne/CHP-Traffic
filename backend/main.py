from selenium import webdriver
from flask import Flask, jsonify
from flask_cors import CORS
import format as format

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=["GET"])
def hello():
    return jsonify({
        'foo': 'bar'
    })

@app.route("/api", methods=["GET"])
def data():
    driver = webdriver.Chrome()
    
    rows = []
    time = []
    type = []
    location = []
    area = []

    # time = ['time']
    # type = ['type']
    # location = ['location']
    # area = ['area']
    
    format.querySequence(driver, rows, time, type, location, area)
    
    driver.close()
    
    return jsonify({
        'time': time,
        'type': type,
        'location': location,
        'area': area
    }), 200
    