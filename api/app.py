"""
Demo Brain API Application

This Flask application serves the demo brain data and provides read-only access to the UNS simulator.
"""

from flask import Flask, jsonify, request
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

app = Flask(__name__)

@app.route('/api/demo-brain')
def get_demo_brain():
    """Return demo brain data from company-brain directory."""
    brain_data = {
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "data": {
            "company": {
                "name": "AI Software Factory (AISF)",
                "type": "company",
                "description": "AI Software Factory is a technology company focused on developing AI-powered solutions and enterprise software products.",
                "founded": "2026",
                "headquarters": "Zurich, Switzerland",
                "industry": "AI Software Development"
            },
            "facts": {
                "total_customers": 25,
                "active_projects": 4,
                "revenue_projection": 1250000.00,
                "customer_satisfaction": 4.2
            },
            "projects": [
                {"name": "Nahum AI OS", "status": "active", "progress": 87.5},
                {"name": "City Intelligence", "status": "active", "progress": 92.3},
                {"name": "Land Intelligence", "status": "active", "progress": 78.9},
                {"name": "Bitdriver", "status": "active", "progress": 65.2}
            ],
            "customers": [
                {"name": "Alcendo AG", "type": "Technology Partner", "status": "active"},
                {"name": "Bitdriver AG", "type": "Product Client", "status": "active"},
                {"name": "City Intelligence AG", "type": "Product Client", "status": "active"},
                {"name": "Land Intelligence AG", "type": "Product Client", "status": "active"}
            ]
        }
    }
    
    return jsonify(brain_data)

@app.route('/api/uns-simulator')
def get_uns_simulator():
    """Return UNS simulator data (read-only)."""
    if not UNS_SIMULATOR_AVAILABLE:
        return jsonify({
            "error": "UNS simulator not available",
            "status": "error"
        }), 500
    
    try:
        data = get_uns_simulator_results()
        return jsonify({
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "data": data
        })
    except Exception as e:
        return jsonify({
            "error": f"Failed to retrieve UNS simulator data: {str(e)}",
            "status": "error"
        }), 500

@app.route('/api/uns-query')
def get_uns_query():
    """Return UNS query tool data (read-only)."""
    if not UNS_SIMULATOR_AVAILABLE:
        return jsonify({
            "error": "UNS query tool not available",
            "status": "error"
        }), 500
    
    try:
        data = get_uns_query_tool_data()
        return jsonify({
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "data": data
        })
    except Exception as e:
        return jsonify({
            "error": f"Failed to retrieve UNS query tool data: {str(e)}",
            "status": "error"
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)