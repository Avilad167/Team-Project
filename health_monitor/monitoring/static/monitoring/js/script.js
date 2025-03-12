document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('alertBtn');
    if (button) {
        button.addEventListener('click', function () {
            alert('Button clicked from external JS!');
        });
    }
});

function fetchSensorData() {
    fetch('/get-sensor-data/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('sensorData').textContent = `Sensor Data: ${data.value}`;

            // Update chart with new data
            renderChart(data);
        })
        .catch(error => {
            console.log('Error fetching data:', error);
            document.getElementById('sensorData').textContent = 'Error fetching data';
        });
}

// Update every 5 seconds
setInterval(fetchSensorData, 5000);

// Initialize chart
let chartInstance;
function renderChart(sensorData) {
    const ctx = document.getElementById('sensorChart').getContext('2d');

    if (chartInstance) {
        chartInstance.destroy(); // Destroy the old chart before creating a new one
    }

    chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: sensorData.labels,
            datasets: [{
                label: 'Sensor Data',
                data: sensorData.values,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        }
    });
}

fetch('/submit-sensor-data/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}'  // Django CSRF token for security
    },
    body: JSON.stringify({ sensorValue: sensorValue })

})
