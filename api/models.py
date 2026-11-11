"""
Data Models for Demo Brain API

This file contains the data models used by the demo brain API.
"""

from dataclasses import dataclass
from typing import List, Dict, Any
from datetime import datetime

@dataclass
class CompanyInfo:
    """Company information model."""
    name: str
    type: str
    description: str
    founded: str
    headquarters: str
    industry: str

@dataclass
class FactsData:
    """Facts data model."""
    total_customers: int
    active_projects: int
    revenue_projection: float
    customer_satisfaction: float

@dataclass
class ProjectInfo:
    """Project information model."""
    name: str
    status: str
    progress: float

@dataclass
class CustomerInfo:
    """Customer information model."""
    name: str
    type: str
    status: str

@dataclass
class BrainData:
    """Demo brain data model."""
    company: CompanyInfo
    facts: FactsData
    projects: List[ProjectInfo]
    customers: List[CustomerInfo]

@dataclass
class UNSSimulatorResults:
    """UNS simulator results model."""
    timestamp: str
    seed: int
    total_customers: int
    active_projects: int
    revenue_projection: float
    customer_satisfaction: float
    employee_count: int
    project_completion_rate: float
    tech_stack_count: int
    data_points_processed: int
    api_calls_today: int
    error_rate: float
    uptime_percentage: float
    monthly_growth: float
    quarterly_revenue: float
    customer_retention: float
    average_response_time: float
    peak_users_today: int
    peak_users_weekend: int

@dataclass
class UNSQueryData:
    """UNS query tool data model."""
    seed: int
    timestamp: str
    companies: List[Dict[str, Any]]
    projects: List[Dict[str, Any]]
    metrics: Dict[str, Any]

@dataclass
class APIResponse:
    """API response model."""
    status: str
    timestamp: str
    data: Dict[str, Any]

class DataValidator:
    """Data validation utilities."""
    
    @staticmethod
    def validate_company_info(data: Dict[str, Any]) -> bool:
        """Validate company information."""
        required_fields = ['name', 'type', 'description', 'founded', 'headquarters', 'industry']
        return all(field in data for field in required_fields)
    
    @staticmethod
    def validate_facts_data(data: Dict[str, Any]) -> bool:
        """Validate facts data."""
        required_fields = ['total_customers', 'active_projects', 'revenue_projection', 'customer_satisfaction']
        return all(field in data for field in required_fields)
    
    @staticmethod
    def validate_json_structure(data: Dict[str, Any], expected_structure: Dict[str, Any]) -> bool:
        """Validate JSON structure against expected schema."""
        # Simple validation - check if required top-level keys exist
        return all(key in data for key in expected_structure.keys())