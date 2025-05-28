# AI Prompts for Live Data Governance Demo

## Prompt 1: Analyzing the Messy Product Data

**Copy this prompt and paste the tobacco_product_inventory_messy.csv content:**

```
I have a tobacco product inventory dataset with cryptic field names. Please analyze this data and provide:

1. Business-friendly names for each field
2. Draft definitions based on the data patterns and values
3. Identify which fields are likely Critical Data Elements (CDEs) for tobacco compliance
4. Suggest data quality rules and validation checks
5. Flag any potential compliance issues you notice

Here's the data:
[PASTE CSV CONTENT HERE]

Please format your response as a structured analysis that could be reviewed by subject matter experts.
```

## Prompt 2: Extracting Knowledge from Regulatory Document

**Copy this prompt and paste the FDA_Compliance_Process_v2.txt content:**

```
Please extract key business terms, data elements, and business rules from this tobacco compliance document. I need:

1. All data field names mentioned and their business definitions
2. Business rules that should be enforced in our data systems  
3. Critical Data Elements (CDEs) for regulatory compliance
4. Data quality checks that should be implemented
5. Any data governance requirements or processes described

Please organize this into a structured format suitable for populating a data catalog.

Document content:
[PASTE DOCUMENT CONTENT HERE]
```

## Prompt 3: Analyzing Scattered Email Knowledge

**Copy this prompt and paste the Sales_Team_Email_Thread.txt content:**

```
This email thread contains scattered tribal knowledge about our data systems. Please extract:

1. Data field definitions and business meanings that are buried in the conversation
2. Data quality issues mentioned and suggested fixes
3. Business rules that should be documented
4. Any data governance gaps or problems identified
5. Critical Data Elements mentioned by the business users

Please consolidate this scattered knowledge into a structured format for our data catalog.

Email thread:
[PASTE EMAIL CONTENT HERE]
```

## Prompt 4: Generating Data Quality Checks

**Use this prompt after analyzing the data:**

```
Based on the tobacco industry data we've analyzed, please suggest comprehensive data quality checks for each field including:

1. Format validation rules
2. Business logic validations  
3. Compliance-specific checks for tobacco regulations
4. Cross-field validation rules
5. Acceptable value ranges and constraints

Focus particularly on FDA compliance requirements and age verification rules for tobacco products.
```

## Prompt 5: Creating Business Glossary

**Use this prompt to consolidate findings:**

```
Please create a comprehensive business glossary for our tobacco company data catalog including:

1. All cryptic field names translated to business-friendly terms
2. Standard definitions for tobacco industry terms
3. Critical Data Elements with compliance justification
4. Data lineage and system sources
5. Business rules and data quality standards

Format this as a business glossary that non-technical stakeholders can understand and use for training new employees.
```

## Demo Script Notes:

### Live Demo Flow:
1. **Show the Problem** (30 seconds)
   - Open tobacco_product_inventory_messy.csv
   - Point out cryptic field names: "What does CAT_CD mean? NIC_MG? COMP_STAT?"
   - Show scattered documents in documents folder

2. **AI Analysis - Part 1** (90 seconds)
   - Use Prompt 1 with the CSV data
   - Show AI generating business-friendly names
   - Highlight Critical Data Elements identified

3. **AI Analysis - Part 2** (90 seconds)  
   - Use Prompt 2 with regulatory document
   - Show AI extracting business rules
   - Demonstrate knowledge extraction from documents

4. **AI Analysis - Part 3** (60 seconds)
   - Use Prompt 3 with email thread
   - Show AI finding scattered tribal knowledge
   - Point out business definitions hidden in emails

5. **Populate Template** (60 seconds)
   - Copy AI outputs into metadata_catalog_template.csv
   - Show structured, reviewable format
   - Highlight SME review workflow

### Key Talking Points:
- "This is our reality - data everywhere, no definitions"
- "AI turns chaos into structure in minutes, not months"
- "Human expertise still crucial - AI just accelerates the heavy lifting"
- "From tribal knowledge to documented standards"
- "Scalable approach for compliance and analytics readiness" 