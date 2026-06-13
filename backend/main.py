from selenium import webdriver

from flask import Flask, jsonify
import backend.format as format

app = Flask(__name__)
@app.route("/", methods=["GET"])
def data():
    driver = webdriver.Chrome()
    
    rows = []
    time = []
    type = []
    location = []
    area = []
    
    format.querySequence(driver, rows, time, type, location, area)
    
    return jsonify({
        'time': time,
        'type': type,
        'location': location,
        'area': area
    }), 200