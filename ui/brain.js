// Brain JavaScript Functionality
// This file handles the UI interactions and data loading for the demo brain application

let currentPage = 'home';

// Navigation functions
function navigateToHome() {
    currentPage = 'home';
    updateNavigation();
    loadHomePage();
}

function navigateToBrain() {
    currentPage = 'brain';
    updateNavigation();
    loadBrainPage();
}

function updateNavigation() {
    // Update active navigation link
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.classList.remove('active');
        if ((currentPage === 'home' && link.textContent.includes('Home')) ||
            (currentPage === 'brain' && link.textContent.includes('Company Brain'))) {
            link.classList.add('active');
        }
    });
}

// Home page functions
async function loadHomePage() {
    const homeSection = document.querySelector('#home');
    homeSection.innerHTML = '<div class="loading">Loading brain data...</div>';
    
    try {
        const brainData = await loadBrainData();
        displayHomeData(brainData);
    } catch (error) {
        console.error('Error loading home page:', error);
        homeSection.innerHTML = '<div class="error">Failed to load brain data. Please try again.</div>';
    }
}

async function loadBrainData() {
    // Try to load from API first
    try {
        const response = await fetch('/api/demo-brain');
        if (response.ok) {
            return await response.json();
        }
    } catch (error) {
        console.log('API not available, using fallback data');
    }
    
    // Fallback to static data
    return {
        "status": "success",
        "timestamp": new Date().toISOString(),
        "data": {
            "company": {
                "name": "AI Software Factory (AISF)",
                "description": "AI Software Factory is a technology company focused on developing AI-powered solutions and enterprise software products."
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
            ]
        }
    };
}

function displayHomeData(data) {
    const homeSection = document.querySelector('#home');
    const brainDataContainer = homeSection.querySelector('#brain-data');
    
    brainDataContainer.innerHTML = `
        <div class="home-dashboard">
            <div class="data-card">
                <h3>Company Overview</h3>
                <p><strong>Name:</strong> ${data.data.company.name}</p>
                <p><strong>Description:</strong> ${data.data.company.description}</p>
            </div>
            
            <div class="data-card">
                <h3>Key Metrics</h3>
                <p><strong>Total Customers:</strong> ${data.data.facts.total_customers}</p>
                <p><strong>Active Projects:</strong> ${data.data.facts.active_projects}</p>
                <p><strong>Revenue Projection:</strong> $${data.data.facts.revenue_projection.toLocaleString()}</p>
                <p><strong>Customer Satisfaction:</strong> ${data.data.facts.customer_satisfaction}/5.0</p>
            </div>
            
            <div class="data-card">
                <h3>Projects Status</h3>
                <ul>
                    ${data.data.projects.map(project => `
                        <li>${project.name}: ${project.progress}% complete</li>
                    `).join('')}
                </ul>
            </div>
            
            <div class="data-card">
                <h3>Quick Actions</h3>
                <button onclick="navigateToBrain()">View Detailed Brain Information</button>
                <button onclick="refreshBrainData()">Refresh Data</button>
            </div>
        </div>
    `;
}

// Brain page functions
async function loadBrainPage() {
    const brainSection = document.querySelector('#brain');
    
    try {
        // Load company information
        await loadCompanyInfo();
        await loadFacts();
        await loadTimeline();
        await loadProjects();
        await loadCustomers();
        await loadUNSSimulatorStatus();
        
        // Update last updated timestamp
        document.querySelector('#last-updated').textContent = new Date().toLocaleString();
        
    } catch (error) {
        console.error('Error loading brain page:', error);
        document.querySelector('#company-info-content').innerHTML = 
            '<div class="error">Failed to load data. Please try again.</div>';
    }
}

async function loadCompanyInfo() {
    const companyContent = document.querySelector('#company-info-content');
    
    try {
        const response = await fetch('/api/demo-brain');
        if (response.ok) {
            const data = await response.json();
            const company = data.data.company;
            
            companyContent.innerHTML = `
                <div class="company-info">
                    <h3>${company.name}</h3>
                    <p><strong>Type:</strong> ${company.type}</p>
                    <p><strong>Industry:</strong> ${company.industry}</p>
                    <p><strong>Founded:</strong> ${company.founded}</p>
                    <p><strong>Headquarters:</strong> ${company.headquarters}</p>
                    <p><strong>Description:</strong> ${company.description}</p>
                    <p><strong>Contact:</strong> info@aisf.ai</p>
                </div>
            `;
        } else {
            throw new Error('Failed to fetch company data');
        }
    } catch (error) {
        console.error('Error loading company info:', error);
        companyContent.innerHTML = '<div class="error">Failed to load company information.</div>';
    }
}

async function loadFacts() {
    const factsContent = document.querySelector('#facts-content');
    
    try {
        const response = await fetch('/api/demo-brain');
        if (response.ok) {
            const data = await response.json();
            const facts = data.data.facts;
            
            factsContent.innerHTML = `
                <div class="facts-grid">
                    <div class="fact-card">
                        <h4>Total Customers</h4>
                        <p class="fact-value">${facts.total_customers}</p>
                    </div>
                    <div class="fact-card">
                        <h4>Active Projects</h4>
                        <p class="fact-value">${facts.active_projects}</p>
                    </div>
                    <div class="fact-card">
                        <h4>Revenue Projection</h4>
                        <p class="fact-value">$${facts.revenue_projection.toLocaleString()}</p>
                    </div>
                    <div class="fact-card">
                        <h4>Customer Satisfaction</h4>
                        <p class="fact-value">${facts.customer_satisfaction}/5.0</p>
                    </div>
                </div>
            `;
        } else {
            throw new Error('Failed to fetch facts data');
        }
    } catch (error) {
        console.error('Error loading facts:', error);
        factsContent.innerHTML = '<div class="error">Failed to load facts data.</div>';
    }
}

async function loadTimeline() {
    const timelineContent = document.querySelector('#timeline-content');
    
    // Static timeline data since it's file-based
    const timelineData = [
        { date: '2026-11-11', event: 'AI-324 demo brain created', source: 'company-brain/company/company.md' },
        { date: '2026-11-10', event: 'Initial demo structure planning', source: 'company-brain/company/company.md' },
        { date: '2026-11-09', event: 'AI-324 requirements analysis', source: 'company-brain/company/company.md' }
    ];
    
    timelineContent.innerHTML = `
        <div class="timeline">
            ${timelineData.map(item => `
                <div class="timeline-item">
                    <div class="timeline-date">${item.date}</div>
                    <div class="timeline-event">${item.event}</div>
                    <div class="timeline-source">${item.source}</div>
                </div>
            `).join('')}
        </div>
    `;
}

async function loadProjects() {
    const projectsContent = document.querySelector('#projects-content');
    
    try {
        const response = await fetch('/api/demo-brain');
        if (response.ok) {
            const data = await response.json();
            const projects = data.data.projects;
            
            projectsContent.innerHTML = `
                <div class="projects-grid">
                    ${projects.map(project => `
                        <div class="project-card">
                            <h4>${project.name}</h4>
                            <p><strong>Status:</strong> ${project.status}</p>
                            <p><strong>Progress:</strong> ${project.progress}%</p>
                            <div class="progress-bar">
                                <div class="progress-fill" style="width: ${project.progress}%"></div>
                            </div>
                        </div>
                    `).join('')}
                </div>
            `;
        } else {
            throw new Error('Failed to fetch projects data');
        }
    } catch (error) {
        console.error('Error loading projects:', error);
        projectsContent.innerHTML = '<div class="error">Failed to load projects data.</div>';
    }
}

async function loadCustomers() {
    const customersContent = document.querySelector('#customers-content');
    
    try {
        const response = await fetch('/api/demo-brain');
        if (response.ok) {
            const data = await response.json();
            const customers = data.data.customers;
            
            customersContent.innerHTML = `
                <div class="customers-grid">
                    ${customers.map(customer => `
                        <div class="customer-card">
                            <h4>${customer.name}</h4>
                            <p><strong>Type:</strong> ${customer.type}</p>
                            <p><strong>Status:</strong> ${customer.status}</p>
                        </div>
                    `).join('')}
                </div>
            `;
        } else {
            throw new Error('Failed to fetch customers data');
        }
    } catch (error) {
        console.error('Error loading customers:', error);
        customersContent.innerHTML = '<div class="error">Failed to load customers data.</div>';
    }
}

async function loadUNSSimulatorStatus() {
    const unsStatusContent = document.querySelector('#uns-simulator-status');
    
    try {
        const response = await fetch('/api/uns-simulator');
        if (response.ok) {
            const data = await response.json();
            const simulatorData = data.data;
            
            unsStatusContent.innerHTML = `
                <div class="uns-status">
                    <div class="status-item">
                        <h4>Seed</h4>
                        <p>${simulatorData.seed}</p>
                    </div>
                    <div class="status-item">
                        <h4>Total Customers</h4>
                        <p>${simulatorData.total_customers}</p>
                    </div>
                    <div class="status-item">
                        <h4>Revenue Projection</h4>
                        <p>$${simulatorData.revenue_projection.toLocaleString()}</p>
                    </div>
                    <div class="status-item">
                        <h4>Customer Satisfaction</h4>
                        <p>${simulatorData.customer_satisfaction}/5.0</p>
                    </div>
                    <div class="status-item">
                        <h4>API Calls Today</h4>
                        <p>${simulatorData.api_calls_today}</p>
                    </div>
                    <div class="status-item">
                        <h4>Uptime</h4>
                        <p>${simulatorData.uptime_percentage}%</p>
                    </div>
                </div>
                <div class="uns-status-footer">
                    <p>Last updated: ${new Date(simulatorData.timestamp).toLocaleString()}</p>
                </div>
            `;
        } else {
            throw new Error('Failed to fetch UNS simulator data');
        }
    } catch (error) {
        console.error('Error loading UNS simulator status:', error);
        unsStatusContent.innerHTML = '<div class="error">Failed to load UNS simulator status.</div>';
    }
}

// Action functions
async function refreshBrainData() {
    const refreshBtn = document.querySelector('.action-btn')
    if (refreshBtn) {
        refreshBtn.textContent = 'Refreshing...';
        refreshBtn.disabled = true;
        
        try {
            await loadBrainPage();
            setTimeout(() => {
                refreshBtn.textContent = 'Refresh Data';
                refreshBtn.disabled = false;
            }, 2000);
        } catch (error) {
            console.error('Error refreshing data:', error);
            refreshBtn.textContent = 'Refresh Data';
            refreshBtn.disabled = false;
        }
    }
}

async function checkUNSSimulator() {
    try {
        const response = await fetch('/api/uns-simulator');
        if (response.ok) {
            const data = await response.json();
            alert(`UNS Simulator Status: Running\nSeed: ${data.data.seed}\nCustomers: ${data.data.total_customers}\nUptime: ${data.data.uptime_percentage}%`);
        } else {
            alert('UNS Simulator: Not Available');
        }
    } catch (error) {
        console.error('Error checking UNS simulator:', error);
        alert('UNS Simulator: Error checking status');
    }
}

async function checkAPIStatus() {
    try {
        const response = await fetch('/health');
        if (response.ok) {
            const data = await response.json();
            alert(`API Status: Healthy\nVersion: ${data.version}\nLast Checked: ${new Date().toLocaleString()}`);
        } else {
            alert('API Status: Unhealthy');
        }
    } catch (error) {
        console.error('Error checking API status:', error);
        alert('API Status: Error checking status');
    }
}

function checkHealth() {
    // This function is called when the health check link is clicked
    // The actual health check is done via checkAPIStatus()
    console.log('Health check requested');
}

// Utility functions
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Initialize the application when the page loads
document.addEventListener('DOMContentLoaded', function() {
    // Determine which page to show based on URL hash
    const hash = window.location.hash || '#home';
    currentPage = hash.replace('#', '');
    
    if (currentPage === 'brain') {
        navigateToBrain();
    } else {
        navigateToHome();
    }
    
    // Set up periodic data refresh
    setInterval(refreshBrainData, 30000); // Refresh every 30 seconds
});

// Handle browser back/forward navigation
window.addEventListener('popstate', function(event) {
    const hash = window.location.hash || '#home';
    currentPage = hash.replace('#', '');
    
    if (currentPage === 'brain') {
        navigateToBrain();
    } else {
        navigateToHome();
    }
});