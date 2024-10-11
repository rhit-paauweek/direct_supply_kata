import http.server
import socketserver
import urllib.parse
import requests
import json


PORT = 8080
API_KEY = '79b26f9fc74e44aeb34152731241110'  
BASE_URL = 'https://api.weatherapi.com/v1/current.json'

#This class handles the HTTP Requests sent to the server 
class WeatherHandler(http.server.SimpleHTTPRequestHandler):
    #Called when the server receives a GET Request
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        if parsed_path.path == '/weather':
            city = query_params.get('city', [''])[0]
            if not city:
                self.send_error(400, "City name is required")
                return

            #These are the parameters required to use the API
            params = {
                'key': API_KEY,
                'q': city
            }
            
            # This makes a GET request and checks if the request is successful
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(weather_data).encode())
            else:
                self.send_error(response.status_code, "Failed to fetch data")
        else:
            super().do_GET()

# This creates and starts the server
with socketserver.TCPServer(("", PORT), WeatherHandler) as httpd:
    print(f"Serving on port {PORT}. Try: http://localhost:{PORT}/weather.html")
    httpd.serve_forever()
