from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Tobacco industry data inventory for the four use cases
data_inventory = {
    "databases": [
        {
            "id": "DB001",
            "name": "Product_Characterization_DB",
            "type": "SQL",
            "description": "Laboratory testing data for tobacco product characterization - Section 2.8, 2.9, 2.10 Standards",
            "owner": "Quality Control Lab",
            "last_updated": "2024-03-15",
            "quality_score": 0.95,
            "use_case": "Product Description (Nonclinical)",
            "standards": ["Section 2.8 Tabulation", "Section 2.9 Analysis", "Section 2.10 Data Exchange"],
            "cde_count": 12
        },
        {
            "id": "DB002",
            "name": "Biomarker_Clinical_DB",
            "type": "NoSQL",
            "description": "Individual health biomarker and exposure data - Section 2.7, 2.9 Standards",
            "owner": "Clinical Research Team",
            "last_updated": "2024-03-14",
            "quality_score": 0.92,
            "use_case": "Product Impact on Individual Health",
            "standards": ["Section 2.7 Collection", "Section 2.9 Analysis"],
            "cde_count": 9
        },
        {
            "id": "DB003",
            "name": "Population_Surveillance_DB",
            "type": "Data Warehouse",
            "description": "Population health surveillance and epidemiological data - Section 2.9 Standards",
            "owner": "Epidemiology Team",
            "last_updated": "2024-03-13",
            "quality_score": 0.89,
            "use_case": "Product Impact on Population Health",
            "standards": ["Section 2.9 Analysis"],
            "cde_count": 8
        },
        {
            "id": "DB004",
            "name": "Regulatory_Compliance_DB",
            "type": "Document Store",
            "description": "Comprehensive regulatory submissions and compliance tracking - All Standards",
            "owner": "Regulatory Affairs",
            "last_updated": "2024-03-15",
            "quality_score": 0.98,
            "use_case": "Comprehensive Regulatory Compliance",
            "standards": ["Section 2.7 Collection", "Section 2.8 Tabulation", "Section 2.9 Analysis", "Section 2.10 Data Exchange"],
            "cde_count": 15
        }
    ],
    "files": [
        {
            "id": "FILE001",
            "name": "product_characterization_messy.csv",
            "type": "CSV",
            "description": "Raw laboratory test data with cryptic field names requiring standardization",
            "owner": "Quality Control Lab",
            "last_updated": "2024-03-13",
            "quality_score": 0.75,
            "use_case": "Product Description (Nonclinical)",
            "fields": ["PROD_CHAR_ID", "NIC_TOT", "TAR_ANHY", "CO_YLD", "FILT_EFF"]
        },
        {
            "id": "FILE002",
            "name": "biomarker_exposure_messy.csv",
            "type": "CSV",
            "description": "Clinical biomarker measurements with inconsistent naming",
            "owner": "Clinical Research Team",
            "last_updated": "2024-03-12",
            "quality_score": 0.82,
            "use_case": "Product Impact on Individual Health",
            "fields": ["SUBJ_ID", "COT_LEVEL", "NNAL_CONC", "AGE_VERIF", "EXP_HIST"]
        },
        {
            "id": "FILE003",
            "name": "surveillance_data_messy.csv",
            "type": "CSV",
            "description": "Population survey data requiring standardization for analysis",
            "owner": "Epidemiology Team",
            "last_updated": "2024-03-11",
            "quality_score": 0.78,
            "use_case": "Product Impact on Population Health",
            "fields": ["SURV_ID", "TOB_USE_PAT", "HEALTH_OUT", "DEMO_DATA"]
        }
    ],
    "apis": [
        {
            "id": "API001",
            "name": "FDA_Submission_API",
            "type": "REST",
            "description": "Real-time FDA submission and compliance tracking",
            "owner": "Regulatory IT",
            "last_updated": "2024-03-15",
            "quality_score": 0.96,
            "use_case": "Comprehensive Regulatory Compliance",
            "endpoints": ["/pmta", "/mrtp", "/compliance", "/labeling"]
        },
        {
            "id": "API002",
            "name": "Laboratory_LIMS_API",
            "type": "SOAP",
            "description": "Laboratory Information Management System integration",
            "owner": "Quality Control",
            "last_updated": "2024-03-14",
            "quality_score": 0.94,
            "use_case": "Product Description (Nonclinical)",
            "endpoints": ["/test-results", "/batch-tracking", "/certifications"]
        }
    ]
}

# Tobacco industry business glossary with CDEs
business_glossary = {
    "Product_ID": {
        "definition": "Unique identifier for tobacco product in FDA submissions",
        "type": "CDE",
        "domain": "Product Management",
        "owner": "Regulatory Affairs",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.10"],
        "regulatory_requirement": "FDA PMTA"
    },
    "Nicotine_Content": {
        "definition": "Total nicotine content measured in mg per cigarette or product unit",
        "type": "CDE", 
        "domain": "Product Characterization",
        "owner": "Quality Control Lab",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.9"],
        "regulatory_requirement": "FDA Testing Standards"
    },
    "Tar_Content": {
        "definition": "Anhydrous tar yield measured under ISO conditions",
        "type": "CDE",
        "domain": "Product Characterization", 
        "owner": "Quality Control Lab",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.9"],
        "regulatory_requirement": "ISO 4387 Standard"
    },
    "Subject_ID": {
        "definition": "Unique clinical study participant identifier with privacy protection",
        "type": "CDE",
        "domain": "Clinical Research",
        "owner": "Clinical Research Team",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "ICH GCP Guidelines"
    },
    "Cotinine_Level": {
        "definition": "Biomarker for nicotine exposure measured in ng/mL",
        "type": "CDE",
        "domain": "Biomarkers",
        "owner": "Clinical Research Team", 
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "Clinical Validation"
    },
    "Age_Verification": {
        "definition": "Confirmed age verification status for tobacco product access",
        "type": "CDE",
        "domain": "Compliance",
        "owner": "Regulatory Affairs",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "21 CFR 1140"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search_data():
    query = request.json.get('query', '').lower()
    use_case_filter = request.json.get('use_case', '')
    
    # Enhanced search with use case filtering
    results = {"databases": [], "files": [], "apis": []}
    
    for db in data_inventory["databases"]:
        if (query in db["name"].lower() or query in db["description"].lower() or 
            query in db["use_case"].lower()):
            if not use_case_filter or use_case_filter in db["use_case"]:
                results["databases"].append(db)
    
    for file in data_inventory["files"]:
        if (query in file["name"].lower() or query in file["description"].lower() or
            query in file["use_case"].lower()):
            if not use_case_filter or use_case_filter in file["use_case"]:
                results["files"].append(file)
                
    for api in data_inventory["apis"]:
        if (query in api["name"].lower() or query in api["description"].lower() or
            query in api["use_case"].lower()):
            if not use_case_filter or use_case_filter in api["use_case"]:
                results["apis"].append(api)
    
    return jsonify(results)

@app.route('/api/glossary', methods=['GET'])
def get_glossary():
    return jsonify(business_glossary)

@app.route('/api/quality', methods=['GET'])
def get_quality_metrics():
    # Tobacco industry specific quality metrics
    return jsonify({
        "overall_score": 0.91,
        "metrics": {
            "regulatory_compliance": 0.98,
            "data_completeness": 0.89,
            "accuracy": 0.94,
            "consistency": 0.87,
            "timeliness": 0.88
        },
        "cde_coverage": {
            "total_fields": 127,
            "standardized_fields": 89,
            "cde_identified": 44,
            "compliance_ready": 89
        },
        "use_case_coverage": {
            "product_description": 0.95,
            "individual_health": 0.92, 
            "population_health": 0.85,
            "regulatory_compliance": 0.98
        }
    })

@app.route('/api/workflow', methods=['POST'])
def initiate_workflow():
    request_data = request.json
    asset_id = request_data.get('asset_id')
    action = request_data.get('action', 'access_request')
    use_case = request_data.get('use_case', '')
    
    # Enhanced workflow with tobacco compliance
    workflow_id = f"TGW{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    compliance_checks = []
    if 'clinical' in use_case.lower():
        compliance_checks.extend(["ICH GCP Validation", "IRB Approval Check"])
    if 'regulatory' in use_case.lower():
        compliance_checks.extend(["FDA Submission Ready", "PMTA Compliance"])
    if 'product' in use_case.lower():
        compliance_checks.extend(["ISO Testing Standards", "Quality Control"])
        
    return jsonify({
        "workflow_id": workflow_id,
        "status": "initiated",
        "message": f"Tobacco governance workflow initiated for {action} on {asset_id}",
        "compliance_checks": compliance_checks,
        "estimated_completion": "2-4 hours",
        "next_steps": ["Regulatory review", "Data steward approval", "Access provisioning"]
    })

@app.route('/api/use-cases', methods=['GET'])
def get_use_cases():
    return jsonify({
        "use_cases": [
            {
                "id": "product_description",
                "name": "Product Description (Nonclinical)",
                "standards": ["Section 2.8 Standards for Tabulation", "Section 2.9 Standards for Analysis", "Section 2.10 Standards for Data Exchange"],
                "description": "Laboratory testing and product characterization data management",
                "assets": 3,
                "cdes": 12
            },
            {
                "id": "individual_health", 
                "name": "Product Impact on Individual Health",
                "standards": ["Section 2.7 Standards for Collection", "Section 2.9 Standards for Analysis"],
                "description": "Clinical studies and biomarker analysis for individual health impact",
                "assets": 2,
                "cdes": 9
            },
            {
                "id": "population_health",
                "name": "Product Impact on Population Health", 
                "standards": ["Section 2.9 Standards for Analysis"],
                "description": "Epidemiological surveillance and population health monitoring",
                "assets": 2,
                "cdes": 8
            },
            {
                "id": "regulatory_compliance",
                "name": "Comprehensive Regulatory Compliance",
                "standards": ["Section 2.7 Standards for Collection", "Section 2.8 Standards for Tabulation", "Section 2.9 Standards for Analysis", "Section 2.10 Standards for Data Exchange"],
                "description": "End-to-end regulatory submission and compliance management",
                "assets": 4,
                "cdes": 15
            }
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001) 