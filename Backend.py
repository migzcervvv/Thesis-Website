from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# Create a Flask app instance
app = Flask(__name__)  
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})
# Configure the database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db = SQLAlchemy(app)

# Define an AirQuality model
class AirQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pm25 = db.Column(db.Float)
    co2 = db.Column(db.Float)

# Set up the Flask application context
with app.app_context():
    # Create the database tables
    db.create_all()
    
    # Insert sample data if there's none yet
    if not AirQuality.query.first():
        sample_data = AirQuality(temperature=22.5, humidity=65, pm25=15, co2=400)
        db.session.add(sample_data)
        db.session.commit()

@app.route('/api/current-air-quality')
def get_current_air_quality():
    # Query the database for the latest air quality data
    latest_data = AirQuality.query.order_by(AirQuality.id.desc()).first()
    
    if not latest_data:
        return jsonify(error="No air quality data available"), 404
    
    air_quality = {
        'temperature': latest_data.temperature,
        'humidity': latest_data.humidity,
        'pm25': latest_data.pm25,
        'co2': latest_data.co2
    }
    return jsonify(air_quality)

@app.route('/api/smog-prediction')
def get_smog_prediction():
    # Sample data for smog prediction
    sample_smog_prediction = {
        'smog_prediction': 'Moderate',
        'recommendation': 'Limit outdoor activities',
    }
    return jsonify(sample_smog_prediction)

if __name__ == '__main__':
    app.run(debug=True)
