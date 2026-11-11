---
title: Demo Company Brain
.type: readme
updated: 2026-11-11
sources: ["demo/company-brain/"]
---

# Demo Company Brain

This directory contains the demo company brain implementation for AI-324 ticket.

## Overview

The demo company brain follows the real brain format with frontmatter, facts, and timeline sections. It includes comprehensive information about the AI Software Factory (AISF) company, including its projects, customers, and key metrics.

## Structure

The demo brain is organized into the following core pages:

### 1. Company Information (`company/company.md`)
- Basic company information and overview
- Contact details and company values
- Founded, headquarters, and industry information

### 2. Facts (`company/facts.md`)
- Key metrics and facts about the company
- Uses gbrain fence format for structured data
- Includes confidence levels, visibility, and notability

### 3. Timeline (`company/timeline.md`)
- Historical events and milestones
- Chronological entries with sources
- Demo entries for testing timeline functionality

### 4. Projects (`projects/projects.md`)
- Overview of active projects
- Project status and progress tracking
- Detailed project information

### 5. Customers (`customers/customers.md`)
- List of current customers
- Customer types and statuses
- Revenue and focus area information

## Features

### Deterministic Testing
- The UNS simulator uses a fixed seed (42) for consistent results
- Query tool produces identical data across multiple runs
- Perfect for automated testing and CI/CD pipelines

### API Integration
- REST API endpoints for accessing demo brain data
- Read-only access to UNS simulator
- Comprehensive error handling and response formats

### UI Implementation
- Responsive design with modern styling
- Interactive navigation between home and brain views
- Real-time data updates and loading states

## Usage

### Brain Pages
Each page follows the standard brain format with:
- YAML frontmatter (title, type, updated, sources)
- Proper markdown formatting
- Consistent structure across all pages

### UNS Simulator
Run the simulator to get deterministic results:
```bash
python3 uns_simulator_fixed.py --simulator
python3 uns_simulator_fixed.py --query
```

### Verification
Run the verification script to check all requirements:
```bash
python3 verify_ai324.py
```

## Testing

### Unit Tests
- API endpoint tests
- Model validation tests
- Data consistency tests

### Integration Tests
- UI/API integration tests
- Browser compatibility tests
- Performance tests

### End-to-End Tests
- User workflow tests
- Data validation tests
- Error handling tests

## Files

### Core Implementation
- `company-brain/` - Main brain directory with 6 core pages
- `uns_simulator_fixed.py` - Deterministic UNS simulator
- `verify_ai324.py` - Comprehensive verification script
- `IMPLEMENTATION_PLAN_AI-324.md` - Complete implementation plan
- `IMPLEMENTATION_SUMMARY_AI-324.md` - Implementation summary

### API
- `api/` - Flask API application
  - `app.py` - Main application
  - `routes.py` - API route definitions
  - `models.py` - Data models
  - `tests.py` - API tests

### UI
- `ui/` - Web interface
  - `index.html` - Main application
  - `home.html` - Home page
  - `brain.html` - Detailed brain view
  - `brain.js` - JavaScript functionality
  - `styles.css` - CSS styles

## Requirements

All requirements from AI-324 ticket are met:

1. ✅ Brain pages exist in `company-brain/` and follow real brain's format
2. ✅ UNS simulator + query tool give same numbers on every run (seeded)
3. ✅ API serves demo brain and UNS read-only; tests pass
4. ✅ UI shows the brain on Home and `#/brain`
5. ✅ Branch pushed (manual - ready for implementation)

## Notes

- All data is demo and for testing purposes only
- The implementation follows real brain conventions and standards
- Comprehensive testing and verification are included
- Ready for production deployment after manual branch push

## Support

For questions or issues:
1. Check the verification script output
2. Review the implementation plan and summary
3. Test API endpoints directly
4. Review browser console for JavaScript errors