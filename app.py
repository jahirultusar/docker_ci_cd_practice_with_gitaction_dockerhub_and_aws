from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Log the incoming request details
    time = datetime.datetime.now()
    print(f"[{time}] Incoming request from IP: {request.remote_addr} | User-Agent: {request.headers.get('User-Agent')}")
    return "Welcome to the Machine - Logging Enabled"

@app.route('/health')
def health_check():
    # In a real app, you'd check DB connections here
    # For now, if this code runs, the app is "Healthy"
    return {"status": "healthy", "uptime": "up"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)