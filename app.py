import os
import time
import socket 
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__) 

# Global start time for the app
start_time = time.time()

# --- ROUTES ---

# Define the storage list
logs_store = []

@app.route('/')
def index():
    """
    Main Landing Page: Now saves logs to memory AND terminal.
    """
    build_time = os.getenv('BUILD_TIME', 'Unknown')
    git_hash = os.getenv('GIT_HASH', 'unknown')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_ip = request.remote_addr
    
    # Create the log string
    log_entry = f"[{timestamp}] Incoming request from {user_ip}"
    
    # 2. Save to our list for the Frontend
    logs_store.append(log_entry)
    if len(logs_store) > 10:  # Keep it tidy - only last 10
        logs_store.pop(0)

    # 3. Keep the print for the Docker Terminal (Objective 3)
    print(log_entry)
    
    return render_template('index.html', build_time=build_time, git_hash=git_hash)

# This is the log route for frontend
@app.route('/api/logs')
def get_logs():
    """Returns the logs_store list as JSON for the JavaScript to read."""
    return jsonify(logs_store)

@app.route('/health')
def health_check():
    """
    Health Check Endpoint.
    Used by the Dockerfile HEALTHCHECK instruction.
    """
    # Returns 200 OK with a JSON body
    return jsonify(status="healthy", timestamp=datetime.now().isoformat()), 200

# API data for frontend
@app.route('/api/health/stats')
def health_stats():
    """
    Advanced Health Data for the Frontend.
    """
    uptime_seconds = int(time.time() - start_time)
    uptime_string = f"{uptime_seconds // 60}m {uptime_seconds % 60}s"
    
    return jsonify(
        status="Healthy",
        uptime=uptime_string,
        pid=os.getpid()
    )


@app.route('/api/logs/clear', methods=['POST'])
def clear_logs():
    """
    Clears the in-memory log list.
    """
    global logs_store
    logs_store = []
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Console logs cleared by user.")
    return jsonify(status="success"), 200

@app.route('/api/network/stats')
def network_stats():
    """
    Objective 4: Network telemetry.
    Using a 'try-except' block to prevent local crashes.
    """
    hostname = socket.gethostname()
    
    # Try to get the IP, but fallback if it fails
    try:
        internal_ip = socket.gethostbyname(hostname)
    except:
        internal_ip = "127.0.0.1 (Local)"

    return jsonify(
        container_id=hostname,
        internal_ip=internal_ip,
        latest_client=request.remote_addr,
        server_time=datetime.now().strftime("%H:%M:%S")
    )



# --- EXECUTION ---

if __name__ == '__main__':
    # Ensure the app listens on all interfaces (0.0.0.0) 
    # and matches the port used in your Dockerfile/Security Group (5001)
    app.run(host='0.0.0.0', port=5001)
