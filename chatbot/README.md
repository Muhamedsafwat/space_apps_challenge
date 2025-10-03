# Abu Simbel Guardian

## Project Overview
The Abu Simbel Guardian is an AI-powered monitoring system that uses NASA satellite data to track and analyze the condition of the Abu Simbel Temple. The system provides real-time insights on foundation movement, environmental conditions, and potential threats to this historical monument.

## Features
- Real-time monitoring of temple foundation movement
- Analysis of environmental factors (temperature, water levels)
- AI-powered chat interface for querying temple status
- Integration with NASA satellite data
- Threat detection and risk assessment

## Project Structure
```
├── api/                  # FastAPI backend
├── data/                 # NASA and temple data
│   ├── processed/        # Processed data files
│   ├── nasa_analysis_results.json
│   └── temple_knowledge.json
├── scripts/              # Data processing utilities
├── src/                  # Core modules
└── requirements.txt      # Project dependencies
```

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Ollama (for local LLM support)

### Installation

1. **cd chatbot **
 
2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   # OR
   # source venv/bin/activate  # On Unix/MacOS
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory with the following variables:
   ```
   OLLAMA_BASE_URL=http://localhost:11434
   MODEL_NAME=llama2
   ```

### Running the Application

#### Backend API
```bash
cd api
python main.py
```
The API will be available at http://localhost:8000

#### Interactive Chat (CLI)
```bash
python run_chat.py
```

## API Endpoints

- `GET /`: API information
- `POST /chat`: Chat with the Abu Simbel Guardian
- `GET /status`: Get current temple status
- `GET /health-summary`: Get detailed health summary
- `POST /reset`: Reset conversation history
- `GET /nasa-data`: Get NASA satellite analysis
- `GET /threats`: Get current threats
- `GET /history`: Get historical events
- `GET /health`: API health check



## Development

### Adding New Data Sources
To add new NASA data sources:
1. Create a new script in the `scripts/` directory
2. Process the data and save to `data/processed/`
3. Update `scripts/integrate_data.py` to include the new data source
