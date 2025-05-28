# 🤖 AI Data Governance Agent Demo

An intelligent data governance agent that automates and streamlines data stewardship tasks using AI and natural language processing.

## 🌟 Features

- **Intelligent Data Discovery**: AI-powered search across databases, files, and APIs
- **Business Glossary Management**: Automated term definition and CDE identification
- **Data Quality Monitoring**: Real-time quality metrics and anomaly detection
- **Workflow Automation**: Streamlined data access and governance processes
- **Natural Language Interface**: Conversational interaction with data assets

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai_agent_demo
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python src/app.py
   ```

5. **Access the demo**:
   Open your browser and navigate to `http://localhost:5000`

## 🎯 Demo Scenarios

### 1. Data Asset Discovery
- Type "customer transactions" in the search bar
- View matching databases, files, and APIs
- Explore metadata and ownership information

### 2. Business Term Analysis
- Browse the business glossary
- Identify Critical Data Elements (CDEs)
- Review term definitions and domains

### 3. Data Quality Assessment
- Monitor real-time quality metrics
- View completeness, accuracy, and consistency scores
- Identify potential data issues

### 4. Access Workflow
- Select a data asset from the dropdown
- Initiate an access request workflow
- Track approval status and progress

## 🛠️ Technical Architecture

### Backend Components
- Flask web server
- RESTful API endpoints
- Mock data stores (replaceable with real databases)
- AI/ML integration points

### Frontend Features
- Modern, responsive UI with Tailwind CSS
- Real-time updates and interactions
- Interactive data visualization
- Workflow management interface

### AI Capabilities
- Natural language processing for search
- Pattern recognition for CDE identification
- Anomaly detection for data quality
- Workflow optimization

## 📊 Data Model

### Data Inventory
```json
{
    "databases": [
        {
            "id": "DB001",
            "name": "Customer_Transactions",
            "type": "SQL",
            "description": "Main customer transaction database",
            "owner": "Finance Team",
            "last_updated": "2024-03-15",
            "quality_score": 0.95
        }
    ]
}
```

### Business Glossary
```json
{
    "Customer_ID": {
        "definition": "Unique identifier for each customer",
        "type": "CDE",
        "domain": "Customer",
        "owner": "Data Governance Team",
        "last_updated": "2024-03-15"
    }
}
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```
FLASK_ENV=development
FLASK_APP=src/app.py
API_KEY=your_api_key_here
```

### Customization Options
- Modify `data_inventory` in `app.py` to connect to real data sources
- Update business glossary with domain-specific terms
- Adjust quality metrics thresholds in the configuration
- Customize workflow templates for your organization

## 📈 Future Enhancements

1. **Advanced AI Integration**
   - GPT-4 for natural language understanding
   - Custom ML models for domain-specific tasks
   - Automated metadata generation

2. **Extended Data Sources**
   - Database connectors for major platforms
   - File system integration
   - API gateway support

3. **Enhanced Workflows**
   - Custom workflow templates
   - Approval routing rules
   - SLA monitoring

4. **Reporting & Analytics**
   - Governance metrics dashboard
   - Compliance reporting
   - Trend analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Flask framework
- Tailwind CSS
- Font Awesome icons
- OpenAI GPT models
- spaCy NLP library 