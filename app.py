"""
Simple Flask Web Application for DevOps Project
This is a sample application to demonstrate DevOps practices.
"""
from flask import Flask, jsonify, render_template_string
import os
import socket
from datetime import datetime

app = Flask(__name__)
start_time = datetime.now()  # Track application start time for metrics

# HTML template for the homepage
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Project - Resume Demo</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { color: #fff; }
        .info { margin: 20px 0; }
        .status { 
            display: inline-block;
            padding: 5px 15px;
            background: #4CAF50;
            border-radius: 20px;
            font-weight: bold;
        }
        .endpoint {
            background: rgba(0, 0, 0, 0.2);
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 DevOps Project - Resume Demo</h1>
        <div class="info">
            <p><strong>Status:</strong> <span class="status">Running</span></p>
            <p><strong>Hostname:</strong> {{ hostname }}</p>
            <p><strong>Environment:</strong> {{ environment }}</p>
            <p><strong>Version:</strong> {{ version }}</p>
            <p><strong>Current Time:</strong> {{ time }}</p>
        </div>
        <h2>Available Endpoints:</h2>
        <div class="endpoint">
            <strong>GET /</strong> - This homepage
        </div>
        <div class="endpoint">
            <strong>GET /health</strong> - Health check endpoint
        </div>
        <div class="endpoint">
            <strong>GET /api/info</strong> - API information
        </div>
        <div class="endpoint">
            <strong>GET /api/metrics</strong> - Application metrics
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Homepage endpoint"""
    hostname = socket.gethostname()
    environment = os.getenv('ENVIRONMENT', 'development')
    version = os.getenv('APP_VERSION', '1.0.0')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template_string(
        HTML_TEMPLATE,
        hostname=hostname,
        environment=environment,
        version=version,
        time=current_time
    )

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes/Docker"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'devops-project'
    }), 200

@app.route('/api/info')
def info():
    """API information endpoint"""
    return jsonify({
        'application': 'DevOps Project - Resume Demo',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'hostname': socket.gethostname(),
        'python_version': os.sys.version,
        'endpoints': {
            '/': 'Homepage',
            '/health': 'Health check',
            '/api/info': 'API information',
            '/api/metrics': 'Application metrics'
        }
    })

@app.route('/api/metrics')
def metrics():
    """Metrics endpoint for Prometheus scraping"""
    # Simple metrics in Prometheus format
    metrics_data = f"""# HELP app_requests_total Total number of requests
# TYPE app_requests_total counter
app_requests_total 1

# HELP app_uptime_seconds Application uptime in seconds
# TYPE app_uptime_seconds gauge
app_uptime_seconds {int((datetime.now() - start_time).total_seconds())}

# HELP app_info Application information
# TYPE app_info gauge
app_info{{version="{os.getenv('APP_VERSION', '1.0.0')}",environment="{os.getenv('ENVIRONMENT', 'development')}"}} 1
"""
    return metrics_data, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)

