"""
API Tests for Demo Brain Application

This file contains tests for the demo brain API endpoints.
"""

import pytest
from flask import Flask
from api.app import app as flask_app
from api.models import BrainData, CompanyInfo, FactsData, ProjectInfo, CustomerInfo

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_health_endpoint(client):
    """Test the health endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert data['version'] == '1.0.0'

def test_demo_brain_endpoint(client):
    """Test the demo brain endpoint."""
    response = client.get('/api/demo-brain')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'timestamp' in data
    assert 'data' in data
    assert 'company' in data['data']
    assert 'facts' in data['data']
    assert 'projects' in data['data']
    assert 'customers' in data['data']

def test_uns_simulator_endpoint(client):
    """Test the UNS simulator endpoint."""
    response = client.get('/api/uns-simulator')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'timestamp' in data
    assert 'data' in data
    
    # Check that UNS simulator data has expected structure
    simulator_data = data['data']
    expected_fields = [
        'timestamp', 'seed', 'total_customers', 'active_projects',
        'revenue_projection', 'customer_satisfaction', 'employee_count',
        'project_completion_rate', 'tech_stack_count', 'data_points_processed',
        'api_calls_today', 'error_rate', 'uptime_percentage', 'monthly_growth',
        'quarterly_revenue', 'customer_retention', 'average_response_time',
        'peak_users_today', 'peak_users_weekend'
    ]
    
    for field in expected_fields:
        assert field in simulator_data

def test_uns_query_endpoint(client):
    """Test the UNS query endpoint."""
    response = client.get('/api/uns-query')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'timestamp' in data
    assert 'data' in data
    
    # Check that UNS query data has expected structure
    query_data = data['data']
    expected_fields = ['seed', 'timestamp', 'companies', 'projects', 'metrics']
    
    for field in expected_fields:
        assert field in query_data

def test_nonexistent_endpoint(client):
    """Test that nonexistent endpoints return 404."""
    response = client.get('/api/nonexistent')
    assert response.status_code == 404
    
    data = response.get_json()
    assert data['status'] == 'error'
    assert 'error' in data

def test_model_validation():
    """Test model validation."""
    # Test CompanyInfo model
    company = CompanyInfo(
        name="Test Company",
        type="company",
        description="Test description",
        founded="2023",
        headquarters="Test City",
        industry="Test Industry"
    )
    assert company.name == "Test Company"
    assert company.type == "company"
    
    # Test FactsData model
    facts = FactsData(
        total_customers=10,
        active_projects=5,
        revenue_projection=100000.0,
        customer_satisfaction=4.5
    )
    assert facts.total_customers == 10
    assert facts.active_projects == 5
    
    # Test ProjectInfo model
    project = ProjectInfo(
        name="Test Project",
        status="active",
        progress=75.0
    )
    assert project.name == "Test Project"
    assert project.status == "active"
    assert project.progress == 75.0
    
    # Test CustomerInfo model
    customer = CustomerInfo(
        name="Test Customer",
        type="Product Client",
        status="active"
    )
    assert customer.name == "Test Customer"
    assert customer.type == "Product Client"
    assert customer.status == "active"

def test_data_validator():
    """Test data validator functions."""
    from api.models import DataValidator
    
    # Test company info validation
    valid_company_data = {
        'name': 'Test Company',
        'type': 'company',
        'description': 'Test description',
        'founded': '2023',
        'headquarters': 'Test City',
        'industry': 'Test Industry'
    }
    
    assert DataValidator.validate_company_info(valid_company_data) == True
    
    invalid_company_data = {
        'name': 'Test Company',
        'type': 'company',
        'description': 'Test description'
    }
    
    assert DataValidator.validate_company_info(invalid_company_data) == False
    
    # Test facts data validation
    valid_facts_data = {
        'total_customers': 10,
        'active_projects': 5,
        'revenue_projection': 100000.0,
        'customer_satisfaction': 4.5
    }
    
    assert DataValidator.validate_facts_data(valid_facts_data) == True
    
    invalid_facts_data = {
        'total_customers': 10,
        'active_projects': 5
    }
    
    assert DataValidator.validate_facts_data(invalid_facts_data) == False
    
    # Test JSON structure validation
    valid_structure = {'key1': 'value1', 'key2': 'value2'}
    test_data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    
    assert DataValidator.validate_json_structure(test_data, valid_structure) == True
    
    invalid_data = {'key1': 'value1'}
    assert DataValidator.validate_json_structure(invalid_data, valid_structure) == False

if __name__ == '__main__':
    pytest.main([__file__, '-v'])