from flask import Flask
import requests
from prometheus_client import Summary, Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metrics
RESPONSE_TIME = Summary('api_response_time_seconds', 'API response time in seconds')
API_STATUS = Gauge('api_up', '1 if API is up, 0 if down')
ERROR_COUNT = Counter('api_error_count', 'Number of API errors')

URL = 'https://httpbin.org/status/503'  # Sample API

@app.route('/probe')
@RESPONSE_TIME.time()
def probe():
    try:
        res = requests.get(URL, timeout=5)
        if res.status_code == 200:
            API_STATUS.set(1)
        else:
            API_STATUS.set(0)
            ERROR_COUNT.inc()
    except:
        API_STATUS.set(0)
        ERROR_COUNT.inc()
    return 'Probed\n'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

    
