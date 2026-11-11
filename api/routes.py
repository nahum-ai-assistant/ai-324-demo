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

@api_bp.route('/demo-brain')
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

@api_bp.route('/uns-simulator')
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

@api_bp.route('/uns-query')
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

@api_bp.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

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