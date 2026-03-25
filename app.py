import os
import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- ROUTES ---

@app.route('/')
def index():
    """
    Main Landing Page: Renders the Bootstrap-enabled dashboard.
    """
    # Log incoming requests to the terminal (viewable via 'docker logs')
    build_time = os.getenv('BUILD_TIME', 'Unknown')
    git_hash = os.getenv('GIT_HASH', 'unknown')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    
    print(f"[{timestamp}] GET / - Request from: {user_ip} | Browser: {user_agent}")
    
    # Renders templates/index.html which extends templates/base.html
    return render_template('index.html', build_time=build_time, git_hash=git_hash)

@app.route('/health')
def health_check():
    """
    Objective 4: Health Check Endpoint.
    Used by the Dockerfile HEALTHCHECK instruction.
    """
    # Returns 200 OK with a JSON body
    return jsonify(status="healthy", timestamp=datetime.datetime.now().isoformat()), 200

# --- EXECUTION ---

if __name__ == '__main__':
    # Objective 2: Ensure the app listens on all interfaces (0.0.0.0) 
    # and matches the port used in your Dockerfile/Security Group (5001)
    app.run(host='0.0.0.0', port=5001)
