# AI Prompts for Population Health Impact Demo

## Prompt 1: Population Health Surveillance Data Analysis

```
I have a population health surveillance dataset for tobacco use patterns and health outcomes across diverse demographic groups. This data comes from large-scale surveys and epidemiological studies designed to assess population-level health impacts. Please analyze this data and provide:

1. Business-friendly names for epidemiological variables following public health standards
2. Draft definitions based on established surveillance methodology and population health metrics
3. Identify Critical Data Elements (CDEs) for population health risk assessment and policy evaluation
4. Suggest data quality rules for survey data integrity and statistical representativeness
5. Flag any issues with survey methodology, population sampling, and epidemiological validity

Focus specifically on:
- Section 2.9 (Standards for Analysis): Statistical analysis for population-level studies

Key population health domains:
- Tobacco use prevalence and patterns by demographics
- Health status and chronic disease associations
- Behavioral risk factors and protective factors
- Social determinants of health
- Geographic and temporal trend analysis

Consider survey design elements:
- Complex sampling design (stratification, clustering, weighting)
- Response bias and non-response adjustments
- Statistical power for subgroup analyses
- Temporal trend detection capabilities

Here's the population surveillance data:
[PASTE CSV CONTENT HERE]

Please format your response as an epidemiological data dictionary suitable for public health analysis and policy development.
```

## Prompt 2: Epidemiological Study Design Assessment

```
Evaluate this population health surveillance dataset for epidemiological study design quality and analytical validity. Focus on:

1. Sampling methodology and population representativeness
2. Survey weighting and stratification adequacy
3. Demographic coverage and subgroup analysis capability
4. Temporal design for trend analysis
5. Data collection standardization across sites/time periods

Assess compliance with:
- CDC surveillance standards
- AAPOR survey methodology guidelines
- Epidemiological study design principles
- Statistical analysis plan requirements

Evaluate potential biases and limitations:
- Selection bias in survey participation
- Recall bias in self-reported behaviors
- Social desirability bias in tobacco use reporting
- Geographic clustering effects

Format as epidemiological study design evaluation report.
```

## Prompt 3: Population Health Metrics and Indicators

```
Create a comprehensive population health metrics framework from this surveillance data including:

1. Prevalence estimates with confidence intervals by key demographics
2. Trend analysis indicators and change detection methods
3. Health disparity measures across population subgroups
4. Risk factor clustering and comorbidity patterns
5. Geographic variation analysis and hotspot identification

Define key population health indicators:
- Tobacco use prevalence rates
- Cessation attempt success rates
- Health outcome associations
- Secondhand smoke exposure levels
- Policy impact assessment metrics

Include statistical methods for:
- Complex survey analysis (weighted estimates)
- Time series analysis for trends
- Multilevel modeling for geographic effects
- Propensity score matching for causal inference
- Meta-analysis across survey cycles

Format as population health surveillance analysis protocol.
```

## Prompt 4: Public Health Policy Data Integration

```
Develop a public health policy analysis framework using this surveillance data including:

1. Policy-relevant outcome measures and targets
2. Health equity assessment across demographic groups
3. Geographic targeting for intervention programs
4. Cost-effectiveness analysis data requirements
5. Evidence synthesis for policy recommendations

Policy analysis domains:
- Tobacco control policy effectiveness
- Health disparities reduction strategies
- Resource allocation optimization
- Public health emergency preparedness
- Community intervention targeting

Data integration requirements:
- Administrative health data linkage
- Economic burden analysis data
- Environmental health factors
- Social determinants integration
- Healthcare utilization patterns

Quality measures for policy analysis:
- Statistical significance testing procedures
- Effect size estimation and clinical significance
- Sensitivity analysis for robust conclusions
- External validity and generalizability assessment

Format as public health policy analysis data specification.
```

## Demo Instructions:

### Live Demo Flow (Population Health Use Case):
1. **Show Survey Complexity** (30 seconds)
   - Display surveillance_data_messy.csv
   - Point out cryptic codes: RESP_ID, AGE_GRP, TOB_USE_STAT, SAMPLE_WGT
   - "How do we analyze population trends with these abbreviated survey codes?"

2. **AI Epidemiological Analysis** (2 minutes)
   - Use Prompt 1 with the CSV data
   - Show AI interpreting survey methodology: "Survey Response ID", "Age Group Category", "Tobacco Use Status"
   - Highlight population sampling weights and statistical considerations

3. **Population Health Insights** (90 seconds)
   - Present health disparity analysis across demographics
   - Show compliance with Section 2.9 (Analysis) for population studies
   - Demonstrate trend analysis and policy-relevant metrics

### Expected Outcomes:
- **24 Population Variables Standardized**: All survey and health variables with epidemiological terminology
- **8 Key Health Indicators as CDEs**: Critical population health metrics for policy
- **95% Survey Data Quality Score**: Enhanced statistical validity and representativeness
- **100% Section 2.9 Analysis Compliance**: Full adherence to population analysis standards

### Key Talking Points:
- "AI understands survey methodology and epidemiological principles"
- "Automated identification of policy-critical health indicators"
- "Population sampling and weighting embedded in analysis framework"
- "Ready for CDC surveillance reporting and policy development"
- "Health disparity patterns emerge from standardized demographic analysis"
- "Geographic hotspots and trend detection enable targeted interventions" 