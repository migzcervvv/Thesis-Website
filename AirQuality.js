document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is running!");

    const airQualityEndpoint = 'http://localhost:5000/api/current-air-quality';
    const smogPredictionEndpoint = 'http://localhost:5000/api/smog-prediction';

    // Fetch the latest air quality data
    fetch(airQualityEndpoint)
        .then(response => {
            console.log('Response Status (Air Quality):', response.status);
            return response.json();
        })
        .then(data => {
            // Update the UI with the fetched data
            document.getElementById('temperature').textContent = data.temperature + ' °C';
            document.getElementById('humidity').textContent = data.humidity + ' %';
            document.getElementById('pm25').textContent = data.pm25 + ' µg/m³';
            document.getElementById('co2').textContent = data.co2 + ' ppm';

            // Construct the payload using the data fetched
            const payload = {
                temperature: data.temperature,
                humidity: data.humidity,
                pm25: data.pm25,
                co2: data.co2,
                humidityTempIndex: data.humidityTempIndex
            };

            // Use this payload to get smog prediction
            fetch(smogPredictionEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            })
            .then(response => {
                console.log('Response Status (Smog Prediction):', response.status);
                return response.json();
            })
            .then(data => {
                const smogLevel = data.smog_prediction;
                updateSmogProgressBar(smogLevel); // Call the function with the smog prediction value
            })
            .catch(error => {
                console.error('Error fetching smog prediction:', error);
            });
        })
        .catch(error => {
            console.error('Error fetching air quality data:', error);
        });
});

document.getElementById('mobile-menu-toggle').addEventListener('click', function() {
    var menu = document.getElementById('navbar-menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
});

function updateSmogProgressBar(smogLevel) {
    const progressBar = document.getElementById('smogProgressBar');
    const recommendationText = document.getElementById('recommendation'); // updated ID

    progressBar.style.width = smogLevel + '%';

    if (smogLevel < 25) {
        progressBar.className = 'progress-bar low';
        recommendationText.textContent = 'Safe to go outside.';
    } else if (smogLevel < 50) {
        progressBar.className = 'progress-bar moderate';
        recommendationText.textContent = 'Moderate smog - consider wearing a mask in polluted areas.';
    } else if (smogLevel < 80) {
        progressBar.className = 'progress-bar high';
        recommendationText.textContent = 'High smog - wear a face mask and avoid polluted areas.';
    } else {
        progressBar.className = 'progress-bar very-high';
        recommendationText.textContent = 'Very high smog - it is advisable to stay indoors.';
    }

    progressBar.textContent = smogLevel.toFixed(2) + '%';
}
