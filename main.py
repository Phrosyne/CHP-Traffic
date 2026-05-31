from selenium import webdriver

from flask import Flask, jsonify
import format

app = Flask(__name__)
@app.route("/")
def hello():
    return "<p>Hello World!</p>"
@app.route("/data", methods=['GET'])
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