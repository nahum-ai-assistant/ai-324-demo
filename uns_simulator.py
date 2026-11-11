#!/usr/bin/env python3
"""
UNS Simulator for AI-324 Demo

This script provides deterministic, seeded results for testing purposes.
All outputs are identical when run with the same seed.
"""

import random
import json
from datetime import datetime

# Fixed seed for deterministic results
SEED = 42
random.seed(SEED)

def get_uns_simulator_results():
    """Return deterministic simulation results."""
    results = {
        "timestamp": datetime.now().isoformat(),
        "seed": SEED,
        "total_customers": 25,
        "active_projects": 4,
        "revenue_projection": 1250000.00,
        "customer_satisfaction": 4.2,
        "employee_count": 178,
        "project_completion_rate": 87.5,
        "tech_stack_count": 12,
        "data_points_processed": 1500000,
        "api_calls_today": 3456,
        "error_rate": 0.02,
        "uptime_percentage": 99.8,
        "monthly_growth": 12.5,
        "quarterly_revenue": 875000.00,
        "customer_retention": 94.2,
        "average_response_time": 145.3,
        "peak_users_today": 89,
        "peak_users_weekend": 45
    }
    return results

def get_uns_query_tool_data():
    """Return deterministic query tool data."""
    data = {
        "seed": SEED,
        "timestamp": datetime.now().isoformat(),
        "companies": [
            {"name": "AI Software Factory", "employees": 178, "revenue": 1250000.00},
            {"name": "City Intelligence AG", "employees": 45, "revenue": 425000.00},
            {"name": "Land Intelligence AG", "employees": 32, "revenue": 380000.00},
            {"name": "Bitdriver AG", "employees": 67, "revenue": 520000.00}
        ],
        "projects": [
            {"name": "Nahum AI OS", "status": "active", "progress": 87.5},
            {"name": "City Intelligence", "status": "active", "progress": 92.3},
            {"name": "Land Intelligence", "status": "active", "progress": 78.9},
            {"name": "Bitdriver", "status": "active", "progress": 65.2}
        ],
        "metrics": {
            "total_customers": 25,
            "active_customers": 23,
            "churned_customers": 2,
            "new_customers": 5,
            "average_contract_value": 50000.00,
            "customer_acquisition_cost": 12000.00,
            "lifetime_value": 180000.00,
            "month_over_month_growth": 12.5
        }
    }
    return data

def main():
    """Main function for CLI usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="UNS Simulator for AI-324 Demo")
    parser.add_argument('--simulator', action='store_true', help='Run UNS simulator')
    parser.add_argument('--query', action='store_true', help='Run UNS query tool')
    parser.add_argument('--output', help='Output file path')
    
    args = parser.parse_args()
    
    results = {}
    
    if args.simulator:
        results['simulator'] = get_uns_simulator_results()
    
    if args.query:
        results['query'] = get_uns_query_tool_data()
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()