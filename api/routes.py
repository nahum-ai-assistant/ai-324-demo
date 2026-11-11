"""
API Routes for Demo Brain Application

This file defines the API routes for accessing demo brain data and UNS simulator.
"""

from flask import Blueprint, jsonify, request
from datetime import datetime
import sys
import os

# Add the demo directory to the path so we can import the UNS simulator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from uns_simulator_fixed import get_uns_simulator_results, get_uns_query_tool_data
    UNS_SIMULATOR_AVAILABLE = True
except ImportError:
    UNS_SIMULATOR_AVAILABLE = False

api_bp = Blueprint('api', __name__, url_prefix='/api')

# All endpoint functions are defined in app.py and imported here

@api_bp.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        "error": "Endpoint not found",
        "status": "error"
    }), 404

@api_bp.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        "error": "Internal server error",
        "status": "error"
    }), 500

# Health check for the main application
@app.route('/')
def index():
    """Root endpoint - health check for the application."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "name": "Demo Brain API Application"
    })