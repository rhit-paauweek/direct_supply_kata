//This functions uses XMLHTTPRequest to communicate with the server
function fetchWeather() {
    const city = document.getElementById('city').value;
    const url = `http://localhost:8080/weather?city=${encodeURIComponent(city)}`;
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            const data = JSON.parse(xhr.responseText);
            displayWeatherData(data);
        } else {
            document.getElementById('weather-data').innerText = `Error: ${xhr.status}`;
        }
    };
    xhr.onerror = function () {
        document.getElementById('weather-data').innerText = 'Network Error';
    };
    xhr.send();
}

//This displays the weater data with the API information
function displayWeatherData(data) {
    const weatherDiv = document.getElementById('weather-data');
    weatherDiv.innerHTML = `
        <h2>Weather in ${data.location.name}, ${data.location.country}</h2>
        <p><strong>Description:</strong> ${data.current.condition.text}</p>
        <p><strong>Temperature (°F):</strong> ${data.current.temp_f}</p>
        <p><strong>Feels Like (°F):</strong> ${data.current.feelslike_f}</p>
        <p><strong>Humidity (%):</strong> ${data.current.humidity}</p>
        <p><strong>Wind Speed (mph):</strong> ${data.current.wind_mph}</p>
    `;
}
