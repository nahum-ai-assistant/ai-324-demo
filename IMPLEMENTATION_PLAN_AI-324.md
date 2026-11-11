# AI-324: Demo Company Brain Implementation Plan

## Overview

This document outlines the comprehensive implementation plan for ticket AI-324, which involves creating a demo company brain with specific functionality for testing and demonstration purposes. The implementation follows the "Done when" requirements outlined in the ticket.

## Requirements Summary

1. **Brain pages exist in `demo/company-brain/` and follow real brain's format (frontmatter, Facts, Timeline)**
2. **UNS simulator + query tool give same numbers on every run (seeded)**
3. **API serves demo brain and UNS read-only; tests pass**
4. **UI shows the brain on Home and `#/brain`**
5. **Branch pushed (manual)**

## Implementation Timeline

### Phase 1: Foundation Setup (Days 1-3)
- Create demo/company-brain directory structure
- Set up README and documentation
- Initialize version control

### Phase 2: Brain Pages Implementation (Days 4-7)
- Create company pages with proper frontmatter
- Implement Facts and Timeline sections
- Create projects and customers overviews
- Ensure all pages follow real brain format

### Phase 3: UNS Simulator Development (Days 8-10)
- Implement seeded UNS simulator
- Create deterministic query tool
- Ensure consistent results across runs
- Add command-line interface

### Phase 4: API Development (Days 11-14)
- Create demo brain API endpoints
- Implement UNS read-only access
- Add API tests
- Set up authentication and authorization

### Phase 5: UI Implementation (Days 15-18)
- Create Home page displaying brain data
- Implement `#/brain` route
- Add responsive design
- Integrate with API backend

### Phase 6: Testing and Validation (Days 19-21)
- Run comprehensive verification tests
- Validate all requirements
- Fix any issues
- Prepare documentation

### Phase 7: Deployment and Documentation (Days 22-25)
- Push branch to repository
- Create user documentation
- Set up monitoring and alerts
- Final review and sign-off

## Detailed Implementation Steps

### Step 1: Create Directory Structure

**Commands:**
```bash
mkdir -p demo/company-brain/company
mkdir -p demo/company-brain/projects
mkdir -p demo/company-brain/customers
mkdir -p demo/api
mkdir -p demo/ui
mkdir -p demo/tests
```

**Files to Create:**
- `demo/README.md` - Overview of demo brain
- `demo/company-brain/README.md` - Demo brain documentation
- `demo/uns_simulator.py` - UNS simulator script
- `demo/verify_ai324.py` - Verification script

### Step 2: Implement Brain Pages

**Required Files and Their Structure:**

#### Company Pages (`demo/company-brain/company/company.md`)
```markdown
---
title: Company Name
type: company
updated: YYYY-MM-DD
sources: ["demo/company-brain/company/"]
---

# Company Information

## Overview
Company description and key information.

## Details
- **Founded**: YYYY-MM-DD
- **Headquarters**: City, Country
- **Industry**: Industry Name
- **Employees**: Number range
- **Website**: URL

## Contact
- **Email**: contact@company.com
- **Phone**: +1-XXX-XXX-XXXX
- **Address**: Full address
```

#### Facts Page (`demo/company-brain/company/facts.md`)
```markdown
---
title: Company Facts
type: company
updated: YYYY-MM-DD
sources: ["demo/company-brain/company/"]
---

# Company Facts

<!--- gbrain:facts:begin -->
# | claim | kind | confidence | visibility | notability | valid_from | valid_until | source | context
---
1 | Metric Name | type | 1.0 | internal | medium | YYYY-MM-DD | | demo/company-brain/company/facts.md | Demo data
2 | Another Metric | type | 1.0 | internal | high | YYYY-MM-DD | | demo/company-brain/company/facts.md | Demo data
<!--- gbrain:facts:end -->
```

#### Timeline Page (`demo/company-brain/company/timeline.md`)
```markdown
---
title: Company Timeline
type: company
updated: YYYY-MM-DD
sources: ["demo/company-brain/company/"]
---

# Company Timeline

- **YYYY-MM-DD** | demo/company-brain/company/timeline.md — Event description
- **YYYY-MM-DD** | demo/company-brain/company/timeline.md — Another event
```

#### Projects Page (`demo/company-brain/projects/projects.md`)
```markdown
---
title: Projects Overview
type: project
updated: YYYY-MM-DD
sources: ["demo/company-brain/projects/"]
---

# Projects Overview

## Active Projects
| Project | Status | Start Date | Completion |
|---------|--------|------------|------------|
| Project Name | active | YYYY-MM-DD | XX% |

## Project Details
- **Project Name**: Description
- **Status**: Current status
- **Progress**: Completion percentage
- **Timeline**: Key milestones
```

#### Customers Page (`demo/company-brain/customers/customers.md`)
```markdown
---
title: Customers Overview
type: customer
updated: YYYY-MM-DD
sources: ["demo/company-brain/customers/"]
---

# Customers Overview

## Current Customers
### Customer Name
- **Type**: Customer type
- **Status**: Active/Inactive
- **Focus**: Business area
- **Revenue**: Revenue range

## Customer Metrics
- **Total Customers**: Number
- **Active Customers**: Number
- **Churned Customers**: Number
- **New Customers**: Number
```

### Step 3: Implement UNS Simulator

**Commands:**
```bash
chmod +x demo/uns_simulator.py
python3 demo/uns_simulator.py --simulator
python3 demo/uns_simulator.py --query
```

**Key Features:**
- Fixed seed for deterministic results (SEED = 42)
- Consistent output across multiple runs
- JSON output for easy parsing
- Command-line interface for flexibility

### Step 4: Create API

**Files to Create:**
- `demo/api/app.py` - Main API application
- `demo/api/routes.py` - API routes
- `demo/api/models.py` - Data models
- `demo/api/tests.py` - API tests

**Example API Structure:**
```python
from flask import Flask, jsonify
from demo.uns_simulator import get_uns_simulator_results, get_uns_query_tool_data

app = Flask(__name__)

@app.route('/api/demo-brain')
def get_demo_brain():
    # Return demo brain data
    pass

@app.route('/api/uns-simulator')
def get_uns_simulator():
    # Return UNS simulator data
    pass

@app.route('/api/uns-query')
def get_uns_query():
    # Return UNS query tool data
    pass

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 5: Implement UI

**Files to Create:**
- `demo/ui/home.html` - Home page
- `demo/ui/brain.html` - Brain page
- `demo/ui/brain.js` - JavaScript for brain interaction
- `demo/ui/styles.css` - CSS styles
- `demo/ui/index.html` - Main index page

**HTML Structure Example:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Demo Company Brain</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="app">
        <header>
            <h1>AI Software Factory - Demo Company Brain</h1>
        </header>
        <main>
            <section id="home">
                <h2>Home</h2>
                <div id="brain-data">
                    <!-- Brain data will be displayed here -->
                </div>
            </section>
            <section id="brain">
                <h2>Company Brain</h2>
                <div id="company-info">
                    <!-- Company information will be displayed here -->
                </div>
                <div id="facts">
                    <!-- Facts table will be displayed here -->
                </div>
                <div id="timeline">
                    <!-- Timeline will be displayed here -->
                </div>
            </section>
        </main>
    </div>
    <script src="brain.js"></script>
</body>
</html>
```

### Step 6: Run Verification Tests

**Commands:**
```bash
chmod +x demo/verify_ai324.py
python3 demo/verify_ai324.py
```

**Verification Script Features:**
- Checks all 5 requirements
- Validates brain page format
- Tests UNS simulator consistency
- Verifies API functionality
- Checks UI implementation
- Provides detailed output

## Verification Commands

### Brain Pages Verification
```bash
# Check if all required files exist and have proper format
python3 -c "
import os
required_files = [
    'demo/company-brain/README.md',
    'demo/company-brain/company/company.md',
    'demo/company-brain/company/facts.md',
    'demo/company-brain/company/timeline.md',
    'demo/company-brain/projects/projects.md',
    'demo/company-brain/customers/customers.md'
]

for file in required_files:
    if os.path.exists(file):
        print(f'✅ {file} exists')
    else:
        print(f'❌ {file} missing')
"
```

### UNS Simulator Verification
```bash
# Test UNS simulator consistency
cd demo
python3 uns_simulator.py --simulator > simulator1.json
python3 uns_simulator.py --simulator > simulator2.json
python3 -c "
import json
with open('simulator1.json') as f:
    data1 = json.load(f)
with open('simulator2.json') as f:
    data2 = json.load(f)

# Remove timestamp for comparison
data1['simulator'].pop('timestamp')
data2['simulator'].pop('timestamp')

if data1 == data2:
    print('✅ UNS simulator produces consistent results')
else:
    print('❌ UNS simulator results differ')
"
```

### UNS Query Tool Verification
```bash
# Test UNS query tool consistency
cd demo
python3 uns_simulator.py --query > query1.json
python3 uns_simulator.py --query > query2.json
python3 -c "
import json
with open('query1.json') as f:
    data1 = json.load(f)
with open('query2.json') as f:
    data2 = json.load(f)

# Remove timestamp for comparison
data1['query'].pop('timestamp')
data2['query'].pop('timestamp')

if data1 == data2:
    print('✅ UNS query tool produces consistent results')
else:
    print('❌ UNS query tool results differ')
"
```

### Full Verification
```bash
# Run complete verification script
cd demo
python3 verify_ai324.py
```

## Testing Strategy

### Unit Tests
- **Brain Pages**: Test frontmatter format and content
- **UNS Simulator**: Test deterministic output
- **UNS Query Tool**: Test data consistency
- **API Endpoints**: Test response formats and authentication

### Integration Tests
- **UI/API Integration**: Test data flow between UI and API
- **Browser Compatibility**: Test in different browsers
- **Performance**: Test response times and data loading

### End-to-End Tests
- **User Workflow**: Test complete user journey
- **Data Validation**: Test data accuracy and consistency
- **Error Handling**: Test error scenarios and recovery

## Quality Assurance

### Code Quality
- Use consistent naming conventions
- Follow markdown formatting standards
- Maintain proper file organization
- Include comprehensive comments

### Documentation
- Update README files
- Document API endpoints
- Provide user guides
- Include troubleshooting sections

### Security
- Validate all inputs
- Implement proper error handling
- Secure sensitive data
- Test for common vulnerabilities

## Rollback Plan

### Immediate Rollback
- Restore from git backup
- Revert all changes
- Clear demo directories
- Restore original state

### Gradual Rollback
- Remove demo files one by one
- Restore original directory structure
- Revert API changes
- Restore original UI files

### Emergency Rollback
- Use git reset --hard
- Restore from backup
- Contact system administrator
- Document rollback steps

## Success Criteria

### Technical Requirements
- All 5 requirements are met
- All verification tests pass
- API endpoints return expected data
- UI displays brain information correctly
- UNS simulator produces consistent results

### Non-Functional Requirements
- Performance meets standards
- Security requirements are satisfied
- Code follows best practices
- Documentation is complete
- Tests cover all functionality

### User Requirements
- Easy to use and navigate
- Clear documentation available
- Responsive design
- Mobile-friendly interface
- Accessible to all users

## Conclusion

This implementation plan provides a comprehensive roadmap for completing ticket AI-324. By following these steps, we can ensure that all requirements are met, the demo company brain is functional, and the implementation is ready for production use.

The plan includes specific commands, verification steps, and quality assurance measures to ensure a successful implementation. All requirements are testable and verifiable through the provided verification scripts.

### Next Steps

1. Begin Phase 1: Foundation Setup
2. Follow the timeline and implementation steps
3. Run verification tests after each phase
4. Address any issues immediately
5. Complete final verification before branch push

This plan ensures that ticket AI-324 is completed successfully with all requirements met and thoroughly tested.