# AI Prompts for Product Description (Nonclinical) Demo

## Prompt 1: Product Characterization Data Analysis

```
I have a tobacco product characterization dataset with cryptic field names used for regulatory submissions. This data covers physical, chemical, and performance testing required for FDA PMTA applications. Please analyze this data and provide:

1. Business-friendly names for each field following FDA tobacco product guidelines
2. Draft definitions based on standard testing methodologies (ISO, CORESTA, etc.)
3. Identify Critical Data Elements (CDEs) required for PMTA submissions under Section 2.8
4. Suggest data quality rules aligned with laboratory testing standards
5. Flag any compliance issues with FDA tobacco product characterization requirements

Focus specifically on:
- Section 2.8 (Standards for Tabulation): Standardized data formats for submission
- Section 2.9 (Standards for Analysis): Statistical analysis requirements  
- Section 2.10 (Standards for Data Exchange): Interoperable data formats

Here's the product characterization data:
[PASTE CSV CONTENT HERE]

Please format your response as a structured analysis suitable for regulatory review and implementation.
```

## Prompt 2: Laboratory Testing Standards Extraction

```
Extract laboratory testing standards and requirements from this product characterization data. Focus on:

1. Test methodology validation (HPLC, GC-MS, gravimetric analysis)
2. Specification limits and acceptable ranges
3. Quality control requirements for each test type
4. Certification status tracking for regulatory compliance
5. Laboratory accreditation and traceability requirements

Identify which tests are mandatory for different product categories:
- Cigarettes (nicotine, tar, CO yields)
- Smokeless tobacco (moisture, pH, microbial)
- Novel tobacco products (emissions, constituents)

Format as regulatory testing protocol documentation.
```

## Prompt 3: Product Specification Standardization

```
Create standardized product specifications from this characterization data for regulatory database integration. Include:

1. Product identification standards (batch numbering, lot tracking)
2. Ingredient composition requirements
3. Physical property specifications (dimensions, weight, filter efficiency)
4. Chemical constituent limits and ranges
5. Performance characteristic standards

Ensure compliance with:
- FDA tobacco product standards
- ISO testing methodology requirements
- CORESTA recommended methods
- Laboratory quality assurance standards

Output as structured product specification template suitable for automated systems.
```

## Prompt 4: Data Quality Framework

```
Develop a comprehensive data quality framework for tobacco product characterization data including:

1. Data validation rules for each measurement type
2. Statistical control limits for laboratory testing
3. Cross-field validation logic (e.g., nicotine vs tar relationships)
4. Outlier detection algorithms for analytical results
5. Completeness requirements for regulatory submissions

Consider:
- Measurement uncertainty and precision requirements
- Inter-laboratory reproducibility standards
- Temporal stability of test results
- Batch-to-batch consistency monitoring

Format as implementable data quality specification.
```

## Demo Instructions:

### Live Demo Flow (Product Description Use Case):
1. **Show Messy Data** (30 seconds)
   - Display product_characterization_messy.csv
   - Point out cryptic codes: CHAR_TYP, TEST_MTH, SPEC_LIM_LOW
   - "What does PC001 mean? T_NIC_001? These codes block regulatory analysis"

2. **AI Analysis** (2 minutes)
   - Use Prompt 1 with the CSV data
   - Show AI generating readable names: "Product Characterization ID", "Nicotine Test Method"
   - Highlight CDE identification for PMTA compliance

3. **Results Showcase** (90 seconds)
   - Present standardized field definitions
   - Show compliance mapping to FDA sections 2.8, 2.9, 2.10
   - Demonstrate data quality rules for laboratory standards

### Expected Outcomes:
- **25 Product Characteristics Standardized**: All testing parameters with business-friendly names
- **12 Critical Data Elements Identified**: Key fields required for FDA submissions
- **90% Time Savings**: Automated vs manual specification development
- **100% Section 2.8 Compliance**: Full adherence to tabulation standards

### Key Talking Points:
- "AI understands ISO testing methods and FDA requirements"
- "Automated identification of PMTA-critical data elements"
- "Laboratory quality standards embedded in data governance"
- "Ready for regulatory submission and database integration" 