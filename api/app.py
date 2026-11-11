"""
Demo Brain API Application

This Flask application serves the demo brain data and provides read-only access to the UNS simulator.
"""

from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import sys
import os
import json
import time
from functools import wraps

# Add the demo directory to the path so we can import the UNS simulator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from uns_simulator_fixed import get_uns_simulator_results, get_uns_query_tool_data
    UNS_SIMULATOR_AVAILABLE = True
except ImportError:
    UNS_SIMULATOR_AVAILABLE = False

# Import API blueprint from routes
from routes import api_bp

# File reading functions
import os

def read_brain_data_from_files():
    """Read brain data from JSON file in company-brain directory."""
    try:
        file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'company-brain',
            'brain_data.json'
        )
        
        with open(file_path, 'r') as f:
            file_data = json.load(f)
            
        # Ensure the data has the expected structure
        if 'data' not in file_data:
            raise ValueError('Missing "data" field in brain data file')
            
        return file_data
    except FileNotFoundError:
        print(f"Warning: Brain data file not found at {file_path}, using fallback data")
        return get_fallback_brain_data()
    except json.JSONDecodeError as e:
        print(f"Warning: Error parsing brain data file: {e}, using fallback data")
        return get_fallback_brain_data()
    except Exception as e:
        print(f"Warning: Error reading brain data from file: {e}, using fallback data")
        return get_fallback_brain_data()

def get_fallback_brain_data():
    """Return fallback brain data when file reading fails."""
    return {
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

# Import the file reading function
brain_data = read_brain_data_from_files()

# API caching
_cache = {}
_cache_ttl = 30  # 30 seconds TTL for cached responses

# Rate limiting
_request_counts = {}
_rate_limit_window = 60  # 1 minute window
_rate_limit_max = 100    # Max requests per window

def simple_auth_required(f):
    """Simple authentication decorator for API endpoints."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for API key in request headers
        api_key = request.headers.get('X-API-Key') or request.args.get('api_key')
        
        # For demo purposes, accept any non-empty API key
        if not api_key:
            return jsonify({
                "error": "API key required",
                "status": "error"
            }), 401
            
        # Add authentication header to response for security
        response = f(*args, **kwargs)
        if hasattr(response, 'headers'):
            response.headers['X-Auth-Status'] = 'authenticated'
            
        return response
    return decorated_function

def cache_response(key, ttl=_cache_ttl):
    """Decorator to cache API responses."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check cache first
            if key in _cache:
                cached_response, timestamp = _cache[key]
                if time.time() - timestamp < ttl:
                    return cached_response
            
            # Call original function
            response = f(*args, **kwargs)
            
            # Cache successful responses
            if response.status_code == 200:
                # Try to get JSON data from response
                try:
                    data = response.get_json()
                    if data and 'status' in data and data['status'] == 'success':
                        # Cache a tuple of (response, timestamp)
                        _cache[key] = (response, time.time())
                except:
                    pass
            
            return response
        return decorated_function
    return decorator

def rate_limit(f):
    """Simple rate limiting decorator."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = request.remote_addr
        current_time = int(time.time())
        
        # Clean old requests from the window
        window_start = current_time - _rate_limit_window
        if client_ip in _request_counts:
            _request_counts[client_ip] = [
                req_time for req_time in _request_counts[client_ip]
                if req_time > window_start
            ]
        else:
            _request_counts[client_ip] = []
        
        # Check rate limit
        if len(_request_counts[client_ip]) >= _rate_limit_max:
            return jsonify({
                "error": "Rate limit exceeded. Please try again later.",
                "status": "error",
                "retry_after": _rate_limit_window
            }), 429
        
        # Record this request
        _request_counts[client_ip].append(current_time)
        
        return f(*args, **kwargs)
    return decorated_function

# Register the API blueprint
app.register_blueprint(api_bp)

@api_bp.route('/demo-brain')
@simple_auth_required
@cache_response('demo_brain')
@rate_limit
def get_demo_brain():
    """Return demo brain data from company-brain directory."""
    return jsonify(brain_data)

@api_bp.route('/uns-simulator')
@simple_auth_required
@cache_response('uns_simulator')
@rate_limit
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
@simple_auth_required
@cache_response('uns_query')
@rate_limit
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
@simple_auth_required
@rate_limit
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)