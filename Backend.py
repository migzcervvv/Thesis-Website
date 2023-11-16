from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db = SQLAlchemy(app)

class AirQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pm25 = db.Column(db.Float)
    co2 = db.Column(db.Float)
    humidityTempIndex = db.Column(db.Float)

with app.app_context():
    db.create_all()
    if not AirQuality.query.first():
        sample_data = AirQuality(
            temperature=32.5,
            humidity=65,
            pm25=15,
            co2=500,
            humidityTempIndex=22.5 * 65
        )
        db.session.add(sample_data)
        db.session.commit()

# Load the machine learning model
with open('Backend/model1.pkl', 'rb') as file:
    stack_model = pickle.load(file)

@app.route('/api/current-air-quality')
def get_current_air_quality():
    latest_data = AirQuality.query.order_by(AirQuality.id.desc()).first()
    if not latest_data:
        return jsonify(error="No air quality data available"), 404

    features = [latest_data.temperature, latest_data.humidity, latest_data.pm25, latest_data.co2, latest_data.humidityTempIndex]
    prediction = stack_model.predict([features])[0]

    air_quality = {
        'temperature': latest_data.temperature,
        'humidity': latest_data.humidity,
        'pm25': latest_data.pm25,
        'co2': latest_data.co2,
        'humidityTempIndex': latest_data.humidityTempIndex,
        'smog_prediction': float(prediction),
        'recommendation': 'Adjust recommendation based on your model\'s output'
    }
    return jsonify(air_quality)

@app.route('/api/smog-prediction', methods=['POST'])
def smog_prediction():
    data = request.get_json()
    features = [data['temperature'], data['humidity'], data['pm25'], data['co2'], data['humidityTempIndex']]
    prediction = stack_model.predict([features])[0]
    return jsonify({'smog_prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)