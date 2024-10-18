from flask import Flask, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
from config import Config

app = Flask(__name__)
CORS(app)

# Load configuration
app.config.from_object(Config)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@"
    f"{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Helper function to query Kedebah API
def query_kedebah_api(endpoint):
    headers = {'Authorization': f'Bearer {Config.API_KEY}'}
    url = f"{Config.KEDEBAH_API_URL}/{endpoint}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error querying Kedebah API: {str(e)}")
        return {'error': str(e)}

# Helper function to query Ticketing Tool API
def query_ticketing_tool_api(endpoint):
    headers = {'Authorization': f'Bearer {Config.API_KEY}'}
    url = f"{Config.TICKETING_TOOL_API_URL}/{endpoint}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error querying Ticketing Tool API: {str(e)}")
        return {'error': str(e)}

# Error handler for internal server errors
@app.errorhandler(500)
def internal_server_error(error):
    logger.error(f"Internal Server Error: {str(error)}")
    return jsonify({'error': 'Internal Server Error'}), 500

# 1. Total Active Projects (cashflow and non-cashflow)
@app.route('/projects/active', methods=['GET'])
def get_active_projects():
    data = query_kedebah_api('projects/active')
    if 'error' in data:
        return jsonify({'error': data['error']}), 500
    return jsonify({'total_active_projects': data})

# 2. Targets Vs Actual
@app.route('/projects/targets-vs-actual', methods=['GET'])
def get_targets_vs_actual():
    data = query_kedebah_api('projects/targets-vs-actual')
    if 'error' in data:
        return jsonify({'error': data['error']}), 500
    return jsonify({'targets_vs_actual': data})

# 3. Timelines Vs Slippages
@app.route('/projects/timelines-vs-slippages', methods=['GET'])
def get_timelines_vs_slippages():
    data = query_kedebah_api('projects/timelines-vs-slippages')
    if 'error' in data:
        return jsonify({'error': data['error']}), 500
    return jsonify({'timelines_vs_slippages': data})

# 4. Activity Output against Service Experience
@app.route('/activity/output-vs-experience', methods=['GET'])
def get_activity_output_vs_experience():
    data = query_kedebah_api('activity/output-vs-experience')
    if 'error' in data:
        return jsonify({'error': data['error']}), 500
    return jsonify({'activity_output_vs_experience': data})

# 5. System Availability Score (from Ticketing tool)
@app.route('/system/availability', methods=['GET'])
def get_system_availability():
    data = query_ticketing_tool_api('system/availability')
    if 'error' in data:
        return jsonify({'error': data['error']}), 500
    return jsonify({'system_availability': data})

# 6. Data Warehouse Availability (from Ticketing tool)
@app.route('/data-warehouse/availability', methods=['GET'])
def get_data_warehouse_availability():
    data = query_ticketing_tool_api('data-warehouse/availability')
    if 'error' in data:
        return jsonify({'error': data['error']}), 500
    return jsonify({'data_warehouse_availability': data})

# 7. Server Response Score (from Ticketing tool)
@app.route('/server/response-score', methods=['GET'])
def get_server_response_score():
    data = query_ticketing_tool_api('server/response-score')
    if 'error' in data:
        return jsonify({'error': data['error']}), 500
    return jsonify({'server_response_score': data})

# 8. Network Latency (from Ticketing tool)
@app.route('/network/latency', methods=['GET'])
def get_network_latency():
    data = query_ticketing_tool_api('network/latency')
    if 'error' in data:
        return jsonify({'error': data['error']}), 500
    return jsonify({'network_latency': data})

if __name__ == '__main__':
    app.run(debug=False)