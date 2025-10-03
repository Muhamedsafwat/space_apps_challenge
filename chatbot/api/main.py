from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.guardian import AbuSimbelGuardian

# Initialize FastAPI
app = FastAPI(
    title="Abu Simbel Digital Guardian API",
    description="AI-powered chatbot for Abu Simbel Temple with NASA satellite monitoring",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global guardian instance
guardian = None

# Request/Response Models
class ChatRequest(BaseModel):
    message: str
    include_history: bool = True

class ChatResponse(BaseModel):
    response: str
    timestamp: str

class StatusResponse(BaseModel):
    health_score: int
    risk_level: str
    foundation_movement_mm: float
    water_level_m: float
    temperature_c: float
    daily_visitors: int

# Startup
@app.on_event("startup")
async def startup_event():
    """Initialize guardian on startup"""
    global guardian
    try:
        print("🔧 Initializing Abu Simbel Guardian...")
        guardian = AbuSimbelGuardian(use_retriever=True)
        print("✅ API ready!")
    except Exception as e:
        print(f"❌ Failed to initialize guardian: {e}")
        raise

# Endpoints
@app.get("/")
async def root():
    """Root endpoint with API info"""
    return {
        "name": "Abu Simbel Digital Guardian API",
        "version": "1.0.0",
        "status": "operational" if guardian else "error",
        "endpoints": {
            "POST /chat": "Chat with Abu Simbel",
            "GET /status": "Get temple health status",
            "GET /health-summary": "Get detailed health summary",
            "POST /reset": "Reset conversation history",
            "GET /nasa-data": "Get NASA satellite analysis",
            "GET /threats": "Get current threats"
        }
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat with the guardian"""
    if guardian is None:
        raise HTTPException(status_code=503, detail="Guardian not initialized")
    
    try:
        from datetime import datetime
        response = guardian.chat(request.message, request.include_history)
        return ChatResponse(
            response=response,
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status")
async def get_status():
    """Get current temple status"""
    if guardian is None:
        raise HTTPException(status_code=503, detail="Guardian not initialized")
    
    try:
        status = guardian.data_loader.temple_data.get('current_status', {})
        return StatusResponse(
            health_score=status.get('health_score', 87),
            risk_level=status.get('risk_level', 'moderate'),
            foundation_movement_mm=status.get('foundation_movement_mm', 0),
            water_level_m=status.get('water_level_lake_nasser', 175),
            temperature_c=status.get('temperature_celsius', 35),
            daily_visitors=status.get('daily_visitors', 8500)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health-summary")
async def health_summary():
    """Get detailed health summary"""
    if guardian is None:
        raise HTTPException(status_code=503, detail="Guardian not initialized")
    
    return {"summary": guardian.get_status_summary()}

@app.post("/reset")
async def reset_conversation():
    """Reset conversation history"""
    if guardian is None:
        raise HTTPException(status_code=503, detail="Guardian not initialized")
    
    guardian.reset_conversation()
    return {"message": "Conversation history cleared"}

@app.get("/nasa-data")
async def get_nasa_data():
    """Get NASA satellite analysis"""
    if guardian is None:
        raise HTTPException(status_code=503, detail="Guardian not initialized")
    
    return guardian.data_loader.nasa_data

@app.get("/threats")
async def get_threats():
    """Get current threats"""
    if guardian is None:
        raise HTTPException(status_code=503, detail="Guardian not initialized")
    
    threats = guardian.data_loader.temple_data.get('threats', [])
    return {"threats": threats}

@app.get("/history")
async def get_history():
    """Get historical events"""
    if guardian is None:
        raise HTTPException(status_code=503, detail="Guardian not initialized")
    
    events = guardian.data_loader.temple_data.get('historical_events', [])
    return {"events": events}

# Health check
@app.get("/health")
async def health_check():
    """API health check"""
    return {
        "status": "healthy",
        "guardian_ready": guardian is not None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)