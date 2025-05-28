# AI Prompts for Individual Health Impact Demo

## Prompt 1: Clinical Biomarker Data Analysis

```
I have a clinical study dataset measuring biomarkers and exposure data for tobacco product health impact assessment. This includes subject demographics, product use patterns, and biomarker measurements from biological samples. Please analyze this data and provide:

1. Business-friendly names for each biomarker and clinical field following medical research standards
2. Draft definitions based on established clinical research protocols and biomarker science
3. Identify Critical Data Elements (CDEs) for individual health risk assessment
4. Suggest data quality rules for clinical data integrity and subject safety
5. Flag any issues with subject privacy (HIPAA), clinical trial compliance (GCP), and regulatory requirements

Focus specifically on:
- Section 2.7 (Standards for Collection): Clinical data collection protocols
- Section 2.9 (Standards for Analysis): Statistical analysis of health outcomes

Key biomarkers to consider:
- Nicotine exposure: Cotinine, nicotine, trans-3'-hydroxycotinine (3HC)
- Tobacco-specific nitrosamines: NNAL (4-(methylnitrosamino)-1-(3-pyridyl)-1-butanol)
- Carcinogen exposure: Benzo[a]pyrene metabolites, phenanthrene
- Physiological markers: Carboxyhemoglobin (COHb)

Here's the clinical biomarker data:
[PASTE CSV CONTENT HERE]

Please format your response as a clinical data dictionary suitable for regulatory submission and medical review.
```

## Prompt 2: Clinical Study Protocol Compliance

```
Review this clinical biomarker dataset for compliance with clinical research standards and regulatory requirements. Focus on:

1. Subject identification and privacy protection measures
2. Visit scheduling and protocol adherence tracking
3. Sample collection and processing standards
4. Laboratory analytical method validation
5. Quality control and quality assurance procedures

Evaluate compliance with:
- FDA Guidance for Clinical Trials
- ICH Good Clinical Practice (GCP) guidelines
- HIPAA privacy regulations
- Clinical laboratory standards (CLIA, CAP)

Identify any protocol deviations, missing data patterns, or quality issues that could impact study integrity or regulatory acceptance.

Format as clinical study compliance assessment report.
```

## Prompt 3: Biomarker Exposure Assessment Framework

```
Create a comprehensive biomarker exposure assessment framework from this clinical data including:

1. Biomarker categorization by exposure pathway and biological significance
2. Reference ranges and clinically significant thresholds
3. Temporal patterns and elimination kinetics considerations
4. Inter-subject variability and demographic factors
5. Product use correlation and dose-response relationships

Consider biomarker classes:
- Nicotine and metabolites (addiction potential)
- Carcinogen biomarkers (cancer risk)
- Inflammatory markers (cardiovascular risk)
- Oxidative stress indicators (cellular damage)

Include statistical analysis requirements for:
- Between-group comparisons
- Longitudinal trend analysis
- Multivariate exposure modeling
- Confounding factor adjustment

Format as biomarker assessment protocol for health impact evaluation.
```

## Prompt 4: Clinical Data Quality and Safety Monitoring

```
Develop clinical data quality monitoring procedures for this biomarker study including:

1. Real-time data validation rules for clinical measurements
2. Subject safety monitoring algorithms and alert thresholds
3. Laboratory result verification and outlier detection
4. Missing data imputation strategies for biomarker analyses
5. Data integrity checks for regulatory compliance

Safety monitoring considerations:
- Adverse event detection from biomarker patterns
- Subject withdrawal criteria based on exposure levels
- Laboratory value monitoring for subject safety
- Protocol deviation tracking and correction procedures

Quality assurance elements:
- Source data verification requirements
- Electronic data capture (EDC) validation
- Statistical analysis plan compliance
- Regulatory submission readiness checks

Format as clinical data management and safety monitoring plan.
```

## Demo Instructions:

### Live Demo Flow (Individual Health Use Case):
1. **Show Clinical Complexity** (30 seconds)
   - Display biomarker_exposure_messy.csv
   - Point out cryptic codes: BIOM_ID, SUBJ_ID, CLIN_SIG
   - "What does BM001 mean? How do we track subject safety with these codes?"

2. **AI Clinical Analysis** (2 minutes)
   - Use Prompt 1 with the CSV data
   - Show AI identifying biomarkers: "Cotinine (Nicotine Metabolite)", "NNAL (Carcinogen Exposure)"
   - Highlight privacy protection and clinical safety considerations

3. **Health Impact Assessment** (90 seconds)
   - Present biomarker categorization for health risk assessment
   - Show compliance with Section 2.7 (Collection) and 2.9 (Analysis)
   - Demonstrate clinical data quality rules and safety monitoring

### Expected Outcomes:
- **24 Clinical Fields Standardized**: All biomarkers and clinical variables with medical terminology
- **9 Biomarkers Identified as CDEs**: Key exposure and health indicators
- **85% Clinical Data Quality Improvement**: Enhanced integrity and safety monitoring
- **100% Section 2.7 & 2.9 Compliance**: Full adherence to clinical collection and analysis standards

### Key Talking Points:
- "AI understands clinical research protocols and biomarker science"
- "Automated identification of health-critical data elements"
- "Subject safety and privacy protection embedded in governance"
- "Ready for FDA health impact assessment and clinical review"
- "Biomarker patterns reveal individual health risk profiles" 