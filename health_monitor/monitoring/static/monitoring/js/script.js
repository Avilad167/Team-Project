document.addEventListener('DOMContentLoaded', function () {
    // ✅ Handle button click event
    const button = document.getElementById('alertBtn');
    if (button) {
        button.addEventListener('click', function () {
            alert('Button clicked from external JS!');
        });
    }

    // ✅ Fetch sensor data initially
    fetchSensorData();

    // ✅ Fetch new sensor data every 5 seconds
    setInterval(fetchSensorData, 5000);
});

// ✅ Function to fetch sensor data from backend
async function fetchSensorData() {
    try {
        const response = await fetch('/get-sensor-data/');
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

        const data = await response.json();
        updateSensorDisplay(data);
        updateChart(data);
    } catch (error) {
        console.error('Error fetching data:', error);
        document.getElementById('sensorData').textContent = 'Error fetching data';
    }
}

// ✅ Update sensor data display
function updateSensorDisplay(data) {
    const sensorDataElement = document.getElementById('sensorData');
    if (sensorDataElement) {
        sensorDataElement.textContent = `Sensor Data: ${data.value}`;
    } else {
        console.warn("Element with ID 'sensorData' not found.");
    }
}

// ✅ Initialize or update the chart
let chartInstance;
function updateChart(sensorData) {
    const canvas = document.getElementById('sensorChart');
    if (!canvas) {
        console.warn("Canvas element for chart not found.");
        return;
    }

    const ctx = canvas.getContext('2d');
    if (!chartInstance) {
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
    } else {
        // ✅ Efficiently update chart without recreating it
        chartInstance.data.labels = sensorData.labels;
        chartInstance.data.datasets[0].data = sensorData.values;
        chartInstance.update();
    }
}

// ✅ Function to submit sensor data securely
async function submitSensorData(sensorValue) {
    try {
        const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
        if (!csrfToken) {
            console.error("CSRF token not found.");
            return;
        }

        const response = await fetch('/submit-sensor-data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ sensorValue })
        });

        const result = await response.json();
        console.log("Data submitted successfully:", result);
    } catch (error) {
        console.error("Error submitting data:", error);
    }
}
