from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Life sciences industry data inventory for the four use cases
data_inventory = {
    "databases": [
        {
            "id": "DB001",
            "name": "Product_Characterization_DB",
            "type": "SQL",
            "description": "Laboratory testing data for product characterization - Section 2.8, 2.9, 2.10 Standards",
            "owner": "Quality Control Lab",
            "last_updated": "2024-03-15",
            "quality_score": 0.95,
            "use_case": "Product Description (Nonclinical)",
            "standards": ["Section 2.8 Tabulation", "Section 2.9 Analysis", "Section 2.10 Data Exchange"],
            "cde_count": 12,
            "tables": ["product_tests", "batch_records", "quality_metrics", "composition_data"],
            "record_count": "2.3M records",
            "data_lineage": "Raw lab instruments → ETL pipeline → Validated database"
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
            "cde_count": 9,
            "collections": ["biomarker_results", "clinical_observations", "adverse_events", "subject_demographics"],
            "record_count": "850K documents",
            "data_lineage": "Clinical sites → EDC system → Data warehouse → Analytics platform"
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
            "cde_count": 8,
            "datasets": ["population_surveys", "health_outcomes", "usage_patterns", "demographic_profiles"],
            "record_count": "12.5M records",
            "data_lineage": "Survey platforms → Data integration → Standardized warehouse → Analytics"
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
            "cde_count": 15,
            "document_types": ["submission_packages", "compliance_reports", "audit_trails", "regulatory_correspondence"],
            "record_count": "45K documents",
            "data_lineage": "Multiple sources → Validation → Regulatory repository → Submission portal"
        }
    ],
    "files": [
        {
            "id": "FILE001",
            "name": "product_characterization_raw.csv",
            "type": "CSV",
            "description": "Raw laboratory test data with cryptic field names requiring standardization",
            "owner": "Quality Control Lab",
            "last_updated": "2024-03-13",
            "quality_score": 0.75,
            "use_case": "Product Description (Nonclinical)",
            "fields": ["PROD_CHAR_ID", "NIC_TOT", "TAR_ANHY", "CO_YLD", "FILT_EFF", "MOIST_CONT", "PH_VAL"],
            "size": "45MB",
            "row_count": "125,000 rows"
        },
        {
            "id": "FILE002",
            "name": "biomarker_exposure_data.csv",
            "type": "CSV",
            "description": "Clinical biomarker measurements with inconsistent naming",
            "owner": "Clinical Research Team",
            "last_updated": "2024-03-12",
            "quality_score": 0.82,
            "use_case": "Product Impact on Individual Health",
            "fields": ["SUBJ_ID", "COT_LEVEL", "NNAL_CONC", "AGE_VERIF", "EXP_HIST", "BMI_VAL", "BP_SYS"],
            "size": "28MB",
            "row_count": "67,500 rows"
        },
        {
            "id": "FILE003",
            "name": "surveillance_population_data.csv",
            "type": "CSV",
            "description": "Population survey data requiring standardization for analysis",
            "owner": "Epidemiology Team",
            "last_updated": "2024-03-11",
            "quality_score": 0.78,
            "use_case": "Product Impact on Population Health",
            "fields": ["SURV_ID", "USE_PAT", "HEALTH_OUT", "DEMO_DATA", "GEO_LOC", "EDU_LEV"],
            "size": "156MB",
            "row_count": "425,000 rows"
        },
        {
            "id": "FILE004",
            "name": "manufacturing_batch_logs.json",
            "type": "JSON",
            "description": "Manufacturing batch records and quality control data",
            "owner": "Manufacturing Operations",
            "last_updated": "2024-03-14",
            "quality_score": 0.91,
            "use_case": "Product Description (Nonclinical)",
            "fields": ["batch_id", "production_date", "quality_checks", "environmental_conditions"],
            "size": "89MB",
            "row_count": "15,750 batches"
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
            "endpoints": ["/pmta", "/mrtp", "/compliance", "/labeling", "/adverse-events"],
            "response_time": "< 200ms",
            "uptime": "99.8%"
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
            "endpoints": ["/test-results", "/batch-tracking", "/certifications", "/equipment-calibration"],
            "response_time": "< 500ms",
            "uptime": "99.5%"
        },
        {
            "id": "API003",
            "name": "Clinical_Data_API",
            "type": "GraphQL",
            "description": "Clinical trial data integration and biomarker access",
            "owner": "Clinical IT",
            "last_updated": "2024-03-13",
            "quality_score": 0.93,
            "use_case": "Product Impact on Individual Health",
            "endpoints": ["/biomarkers", "/adverse-events", "/demographics", "/exposure-data"],
            "response_time": "< 300ms",
            "uptime": "99.7%"
        }
    ]
}

# Life sciences industry business glossary with CDEs
business_glossary = {
    "Product_ID": {
        "definition": "Unique identifier for product in FDA submissions",
        "type": "CDE",
        "domain": "Product Management",
        "owner": "Regulatory Affairs",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.10"],
        "regulatory_requirement": "FDA PMTA",
        "use_cases": ["Product Description (Nonclinical)", "Comprehensive Regulatory Compliance"],
        "data_type": "VARCHAR(20)",
        "example_values": ["PRD-2024-001", "PRD-2024-002"]
    },
    "Nicotine_Content": {
        "definition": "Total nicotine content measured in mg per cigarette or product unit",
        "type": "CDE", 
        "domain": "Product Characterization",
        "owner": "Quality Control Lab",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.9"],
        "regulatory_requirement": "FDA Testing Standards",
        "use_cases": ["Product Description (Nonclinical)", "Product Impact on Individual Health", "Comprehensive Regulatory Compliance"],
        "data_type": "DECIMAL(5,2)",
        "example_values": ["12.5", "8.3", "15.7"]
    },
    "Tar_Content": {
        "definition": "Anhydrous tar yield measured under ISO conditions",
        "type": "CDE",
        "domain": "Product Characterization", 
        "owner": "Quality Control Lab",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.9"],
        "regulatory_requirement": "ISO 4387 Standard",
        "use_cases": ["Product Description (Nonclinical)", "Comprehensive Regulatory Compliance"],
        "data_type": "DECIMAL(4,1)",
        "example_values": ["10.5", "8.2", "12.8"]
    },
    "Subject_ID": {
        "definition": "Unique clinical study participant identifier with privacy protection",
        "type": "CDE",
        "domain": "Clinical Research",
        "owner": "Clinical Research Team",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "ICH GCP Guidelines",
        "use_cases": ["Product Impact on Individual Health", "Product Impact on Population Health", "Comprehensive Regulatory Compliance"],
        "data_type": "VARCHAR(15)",
        "example_values": ["SUB-001-2024", "SUB-002-2024"]
    },
    "Cotinine_Level": {
        "definition": "Biomarker for nicotine exposure measured in ng/mL",
        "type": "CDE",
        "domain": "Biomarkers",
        "owner": "Clinical Research Team", 
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "Clinical Validation",
        "use_cases": ["Product Impact on Individual Health", "Product Impact on Population Health", "Comprehensive Regulatory Compliance"],
        "data_type": "DECIMAL(8,2)",
        "example_values": ["125.50", "87.25", "203.75"]
    },
    "Age_Verification": {
        "definition": "Confirmed age verification status for product access",
        "type": "CDE",
        "domain": "Compliance",
        "owner": "Regulatory Affairs",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "21 CFR 1140",
        "use_cases": ["Product Impact on Individual Health", "Product Impact on Population Health", "Comprehensive Regulatory Compliance"],
        "data_type": "BOOLEAN",
        "example_values": ["true", "false"]
    },
    "Manufacturing_Date": {
        "definition": "Date of product manufacturing for batch tracking",
        "type": "CDE",
        "domain": "Manufacturing",
        "owner": "Manufacturing Operations",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.10"],
        "regulatory_requirement": "FDA Manufacturing Standards",
        "use_cases": ["Product Description (Nonclinical)", "Comprehensive Regulatory Compliance"],
        "data_type": "DATE",
        "example_values": ["2024-03-15", "2024-03-14"]
    },
    "Clinical_Endpoint": {
        "definition": "Primary or secondary endpoint measured in clinical studies",
        "type": "CDE",
        "domain": "Clinical Research",
        "owner": "Clinical Research Team",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "ICH E6 Guidelines",
        "use_cases": ["Product Impact on Individual Health", "Comprehensive Regulatory Compliance"],
        "data_type": "VARCHAR(100)",
        "example_values": ["Reduction in biomarker levels", "Change in lung function"]
    },
    "Population_Demographics": {
        "definition": "Age, gender, and geographic distribution of use population",
        "type": "CDE",
        "domain": "Epidemiology",
        "owner": "Public Health Team",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.9"],
        "regulatory_requirement": "CDC Surveillance Standards",
        "use_cases": ["Product Impact on Population Health", "Comprehensive Regulatory Compliance"],
        "data_type": "JSON",
        "example_values": ["{\"age_group\": \"25-34\", \"gender\": \"M\", \"region\": \"Northeast\"}"]
    },
    "Exposure_Biomarker": {
        "definition": "Biological indicators of product exposure in study populations",
        "type": "CDE",
        "domain": "Biomarkers",
        "owner": "Clinical Research Team",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "FDA Biomarker Qualification",
        "use_cases": ["Product Impact on Individual Health", "Product Impact on Population Health", "Comprehensive Regulatory Compliance"],
        "data_type": "DECIMAL(10,3)",
        "example_values": ["45.125", "67.890", "23.456"]
    },
    "Batch_Number": {
        "definition": "Unique manufacturing batch identifier for product traceability",
        "type": "CDE",
        "domain": "Manufacturing",
        "owner": "Manufacturing Operations",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.10"],
        "regulatory_requirement": "FDA Manufacturing Standards",
        "use_cases": ["Product Description (Nonclinical)", "Comprehensive Regulatory Compliance"],
        "data_type": "VARCHAR(12)",
        "example_values": ["BTH-240315-A", "BTH-240315-B"]
    },
    "Quality_Score": {
        "definition": "Composite quality assessment score for product batches",
        "type": "CDE",
        "domain": "Quality Control",
        "owner": "Quality Control Lab",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.9"],
        "regulatory_requirement": "ISO Quality Standards",
        "use_cases": ["Product Description (Nonclinical)", "Comprehensive Regulatory Compliance"],
        "data_type": "DECIMAL(3,2)",
        "example_values": ["0.95", "0.87", "0.92"]
    },
    "Study_Protocol_ID": {
        "definition": "Unique identifier for clinical study protocol",
        "type": "CDE",
        "domain": "Clinical Research",
        "owner": "Clinical Research Team",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "ICH GCP Guidelines",
        "use_cases": ["Product Impact on Individual Health", "Comprehensive Regulatory Compliance"],
        "data_type": "VARCHAR(20)",
        "example_values": ["PROT-2024-001", "PROT-2024-002"]
    },
    "Adverse_Event_Code": {
        "definition": "Standardized code for adverse events following product exposure",
        "type": "CDE",
        "domain": "Safety",
        "owner": "Safety Team",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.7", "Section 2.9"],
        "regulatory_requirement": "MedDRA Coding",
        "use_cases": ["Product Impact on Individual Health", "Product Impact on Population Health", "Comprehensive Regulatory Compliance"],
        "data_type": "VARCHAR(10)",
        "example_values": ["AE001", "AE002", "AE003"]
    },
    "Regulatory_Status": {
        "definition": "Current regulatory approval status for product",
        "type": "CDE",
        "domain": "Regulatory Affairs",
        "owner": "Regulatory Affairs",
        "last_updated": "2024-03-15",
        "standards": ["Section 2.8", "Section 2.10"],
        "regulatory_requirement": "FDA Submission Requirements",
        "use_cases": ["Product Description (Nonclinical)", "Comprehensive Regulatory Compliance"],
        "data_type": "VARCHAR(20)",
        "example_values": ["Approved", "Under Review", "Submitted"]
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
    use_case_filter = request.args.get('use_case', '')
    
    if use_case_filter:
        # Filter glossary by use case
        filtered_glossary = {}
        for term, data in business_glossary.items():
            if use_case_filter in data.get('use_cases', []):
                filtered_glossary[term] = data
        return jsonify(filtered_glossary)
    else:
        return jsonify(business_glossary)

@app.route('/api/quality', methods=['GET'])
def get_quality_metrics():
    use_case_filter = request.args.get('use_case', '')
    
    # Base quality metrics
    base_metrics = {
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
    }
    
    # Use case specific adjustments
    if use_case_filter:
        use_case_metrics = {
            "Product Description (Nonclinical)": {
                "overall_score": 0.95,
                "cde_coverage": {"total_fields": 45, "standardized_fields": 42, "cde_identified": 15, "compliance_ready": 42},
                "focus_areas": ["Product Characterization", "Manufacturing", "Quality Control"]
            },
            "Product Impact on Individual Health": {
                "overall_score": 0.92,
                "cde_coverage": {"total_fields": 38, "standardized_fields": 35, "cde_identified": 12, "compliance_ready": 35},
                "focus_areas": ["Clinical Research", "Biomarkers", "Subject Safety"]
            },
            "Product Impact on Population Health": {
                "overall_score": 0.85,
                "cde_coverage": {"total_fields": 28, "standardized_fields": 24, "cde_identified": 8, "compliance_ready": 24},
                "focus_areas": ["Epidemiology", "Population Demographics", "Public Health"]
            },
            "Comprehensive Regulatory Compliance": {
                "overall_score": 0.98,
                "cde_coverage": {"total_fields": 127, "standardized_fields": 124, "cde_identified": 44, "compliance_ready": 124},
                "focus_areas": ["All Domains", "Cross-functional Integration", "Regulatory Readiness"]
            }
        }
        
        if use_case_filter in use_case_metrics:
            specific_metrics = use_case_metrics[use_case_filter]
            base_metrics["overall_score"] = specific_metrics["overall_score"]
            base_metrics["cde_coverage"].update(specific_metrics["cde_coverage"])
            base_metrics["focus_areas"] = specific_metrics["focus_areas"]
    
    return jsonify(base_metrics)

@app.route('/api/workflow', methods=['POST'])
def initiate_workflow():
    request_data = request.json
    asset_id = request_data.get('asset_id')
    action = request_data.get('action', 'access_request')
    use_case = request_data.get('use_case', '')
    
    # Enhanced workflow with life sciences compliance
    workflow_id = f"DGW{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    compliance_checks = []
    if 'clinical' in use_case.lower():
        compliance_checks.extend(["ICH GCP Validation", "IRB Approval Check", "Clinical Data Integrity"])
    if 'regulatory' in use_case.lower():
        compliance_checks.extend(["FDA Submission Ready", "PMTA Compliance", "Regulatory Documentation"])
    if 'product' in use_case.lower():
        compliance_checks.extend(["ISO Testing Standards", "Quality Control", "Manufacturing Compliance"])
        
    return jsonify({
        "workflow_id": workflow_id,
        "status": "initiated",
        "message": f"Data governance workflow initiated for {action} on {asset_id}",
        "compliance_checks": compliance_checks,
        "estimated_completion": "2-4 hours",
        "next_steps": ["Regulatory review", "Data steward approval", "Access provisioning"],
        "workflow_details": {
            "stage_1": "Data validation and quality checks",
            "stage_2": "Compliance and regulatory review",
            "stage_3": "Approval and access provisioning",
            "stage_4": "Audit trail generation"
        }
    })

@app.route('/api/use-cases', methods=['GET'])
def get_use_cases():
    return jsonify({
        "use_cases": [
            {
                "id": "product_description",
                "name": "Product Description (Nonclinical)",
                "icon": "🧪",
                "standards": ["Section 2.8 Standards for Tabulation", "Section 2.9 Standards for Analysis", "Section 2.10 Standards for Data Exchange"],
                "fda_section": "Sections 2.8, 2.9, 2.10",
                "description": "Laboratory testing and product characterization data management",
                "assets": 3,
                "cdes": 12
            },
            {
                "id": "individual_health", 
                "name": "Product Impact on Individual Health",
                "icon": "👤",
                "standards": ["Section 2.7 Standards for Collection", "Section 2.9 Standards for Analysis"],
                "fda_section": "Sections 2.7, 2.9",
                "description": "Clinical studies and biomarker analysis for individual health impact",
                "assets": 2,
                "cdes": 9
            },
            {
                "id": "population_health",
                "name": "Product Impact on Population Health",
                "icon": "👥",
                "standards": ["Section 2.9 Standards for Analysis"],
                "fda_section": "Section 2.9",
                "description": "Epidemiological surveillance and population health monitoring",
                "assets": 2,
                "cdes": 8
            },
            {
                "id": "regulatory_compliance",
                "name": "Comprehensive Regulatory Compliance",
                "icon": "📋",
                "standards": ["Section 2.7 Standards for Collection", "Section 2.8 Standards for Tabulation", "Section 2.9 Standards for Analysis", "Section 2.10 Standards for Data Exchange"],
                "fda_section": "Sections 2.7-2.10",
                "description": "End-to-end regulatory submission and compliance management",
                "assets": 4,
                "cdes": 15
            }
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001) 