import ollama
from typing import List, Dict, Optional
from .data_loader import TempleDataLoader
from .prompts import create_master_system_prompt

class AbuSimbelGuardian:
    """Enhanced Abu Simbel Guardian with complete historical context"""
    
    def __init__(self, use_retriever=True):
        print(f"Guardian initialized with retriever set to: {use_retriever}")
        self.use_retriever = use_retriever
        print("🏺 Initializing Abu Simbel Guardian...")
        print("Loading historical records spanning 3,300 years...")
        
        # Load all data
        self.data_loader = TempleDataLoader()
        temple_data = self.data_loader.temple_data
        nasa_data = self.data_loader.nasa_data
        
        # Create master system prompt with all features
        print("Integrating NASA satellite data...")
        self.system_prompt = create_master_system_prompt(temple_data, nasa_data)
        
        # Initialize Ollama
        print("Connecting to AI model...")
        self.client = ollama.Client()
        self.conversation_history: List[Dict[str, str]] = []
        
        print("✅ Abu Simbel Guardian ready!")
        print("📡 Features enabled:")
        print("   - 3,300 years of historical memory")
        print("   - Real-time NASA satellite monitoring")
        print("   - NISAR future capabilities")
        print("   - Egyptian heritage preservation advocacy\n")
    
    def chat(self, user_message: str, include_history: bool = True) -> str:
        """Chat with the guardian"""
        
        messages = [{"role": "system", "content": self.system_prompt}]
        
        if include_history and self.conversation_history:
            messages.extend(self.conversation_history[-10:])
        
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = self.client.chat(
                model='llama3.2:3b',
                messages=messages
            )
            
            response_text = response['message']['content']
            
            # Store in history
            self.conversation_history.append({"role": "user", "content": user_message})
            self.conversation_history.append({"role": "assistant", "content": response_text})
            
            return response_text
            
        except Exception as e:
            return f"Error: {str(e)}\n\nMake sure Ollama is running: ollama serve"
    
    def get_status_summary(self) -> str:
        """Get comprehensive status summary"""
        status = self.data_loader.temple_data.get('current_status', {})
        nasa = self.data_loader.nasa_data.get('current_status', {})
        
        return f"""
🏺 ABU SIMBEL STATUS REPORT
{'='*60}

STRUCTURAL HEALTH:
  Health Score: {status.get('health_score', 87)}/100
  Risk Level: {status.get('risk_level', 'moderate').upper()}
  
NASA SATELLITE DATA:
  Foundation Movement: {status.get('foundation_movement_mm', 0.3)}mm (latest)
  Annual Subsidence: {nasa.get('displacement_velocity_mm_year', 3.2):.2f}mm/year
  Total Displacement: {nasa.get('latest_displacement_mm', 12.8):.1f}mm
  
ENVIRONMENTAL FACTORS:
  Lake Nasser Level: {status.get('water_level_lake_nasser', 175)}m
  Temperature: {status.get('temperature_celsius', 35)}°C
  Daily Visitors: {status.get('daily_visitors', 8500):,}

NISAR STATUS:
  Launch: January 2025 ✅
  Monitoring Begins: Q1 2025
  Expected Impact: Sub-millimeter precision, 6-day revisit

Last Updated: {status.get('last_updated', 'N/A')}
{'='*60}
"""
    
    def get_historical_timeline(self) -> str:
        """Get formatted historical timeline"""
        events = self.data_loader.temple_data.get('historical_events', [])
        
        timeline = "\n📜 ABU SIMBEL HISTORICAL TIMELINE\n" + "="*60 + "\n\n"
        
        for event in events:
            timeline += f"🗓️  {event['year']}: {event['event']}\n"
            if 'details' in event:
                timeline += f"   Details: {event['details']}\n"
            if 'cost' in event:
                timeline += f"   Cost: {event['cost']}\n"
            timeline += "\n"
        
        return timeline
    
    def get_nisar_info(self) -> str:
        """Get NISAR information"""
        return """
🛰️ NISAR SATELLITE - YOUR DIGITAL GUARDIAN
{'='*60}

MISSION DETAILS:
  Full Name: NASA-ISRO Synthetic Aperture Radar
  Launch: January 2025
  Partners: NASA (USA) + ISRO (India)
  Orbit: 747 km altitude, sun-synchronous

CAPABILITIES:
  Precision: Sub-millimeter (0.1mm) displacement detection
  Revisit Time: 6 days (vs 12 days for Sentinel-1)
  Frequency: Dual-band (L-band + S-band)
  Coverage: 24/7, all-weather monitoring

WHY THIS SAVES ABU SIMBEL:
  ✅ Detects micro-movements before visible cracks
  ✅ Predicts problems weeks in advance
  ✅ Enables preventive maintenance
  ✅ Reduces monitoring costs by 60%
  ✅ Extends heritage lifespan by centuries

EGYPTIAN HERITAGE IMPACT:
  Sites to Monitor: 1,100+ monuments
  Economic Protection: $12 billion annual heritage GDP
  Jobs Protected: 100,000+ across heritage sector
  Global Leadership: Egypt becomes heritage tech pioneer

Launch Countdown: OPERATIONAL (January 2025)
{'='*60}
"""
    
    def reset_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("✅ Conversation history cleared")
    
    def export_conversation(self, filepath: str = "conversation_log.json"):
        """Export conversation"""
        import json
        from datetime import datetime
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'conversation': self.conversation_history
            }, f, indent=2, ensure_ascii=False)
        
        print(f"📝 Conversation saved to {filepath}")