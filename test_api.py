#!/usr/bin/env python3
"""
Simple API test script for the Demo Brain Application
"""

import json
import requests
import sys
from datetime import datetime

def test_api_endpoints():
    """Test all API endpoints."""
    print("Testing Demo Brain API...")
    print("=" * 50)
    
    # Test base URL (should redirect to index)
    print("\n1. Testing Health Endpoint...")
    try:
        response = requests.get('http://localhost:5000/health', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Health check passed: {data['status']}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"   ⚠️  Health check error: {e}")
    
    # Test demo brain endpoint
    print("\n2. Testing Demo Brain Endpoint...")
    try:
        response = requests.get('http://localhost:5000/api/demo-brain', timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                print(f"   ✅ Demo brain endpoint passed")
                print(f"   📊 Company: {data['data']['company']['name']}")
                print(f"   📊 Customers: {data['data']['facts']['total_customers']}")
            else:
                print(f"   ❌ Demo brain endpoint failed: {data['status']}")
        else:
            print(f"   ❌ Demo brain endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"   ⚠️  Demo brain endpoint error: {e}")
    
    # Test UNS simulator endpoint
    print("\n3. Testing UNS Simulator Endpoint...")
    try:
        response = requests.get('http://localhost:5000/api/uns-simulator', timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                print(f"   ✅ UNS simulator endpoint passed")
                print(f"   🧠 Seed: {data['data']['seed']}")
                print(f"   📊 Total Customers: {data['data']['total_customers']}")
            else:
                print(f"   ❌ UNS simulator endpoint failed: {data['status']}")
        else:
            print(f"   ❌ UNS simulator endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"   ⚠️  UNS simulator endpoint error: {e}")
    
    # Test UNS query endpoint
    print("\n4. Testing UNS Query Endpoint...")
    try:
        response = requests.get('http://localhost:5000/api/uns-query', timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                print(f"   ✅ UNS query endpoint passed")
                print(f"   🔍 Companies: {len(data['data']['companies'])}")
                print(f"   📈 Metrics: {data['data']['metrics']['month_over_month_growth']}% growth")
            else:
                print(f"   ❌ UNS query endpoint failed: {data['status']}")
        else:
            print(f"   ❌ UNS query endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"   ⚠️  UNS query endpoint error: {e}")
    
    print("\n" + "=" * 50)
    print("API Testing Complete")

if __name__ == '__main__':
    test_api_endpoints()