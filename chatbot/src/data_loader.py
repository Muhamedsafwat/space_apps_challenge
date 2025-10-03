import json
from pathlib import Path
from typing import Dict, Any

class TempleDataLoader:
    """Load and manage temple and NASA data"""
    
    def __init__(self, 
                 temple_data_path: str = "data/temple_knowledge.json",
                 nasa_data_path: str = "data/nasa_analysis_results.json"):
        self.temple_data = self._load_json(temple_data_path)
        self.nasa_data = self._load_json(nasa_data_path)
    
    def _load_json(self, path: str) -> Dict[str, Any]:
        """Load JSON file"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Warning: {path} not found, using empty data")
            return {}
        except json.JSONDecodeError:
            print(f"⚠️  Warning: Invalid JSON in {path}")
            return {}
    
    def get_complete_context(self) -> str:
        """Get formatted context for AI"""
        context_parts = []
        
        # Temple info
        info = self.temple_data.get('temple_info', {})
        context_parts.append(f"""
TEMPLE IDENTITY:
- Built {info.get('age_years', 3300)} years ago by {info.get('built_by', 'Ramesses II')}
- Location: {info.get('location', 'Aswan, Egypt')}
- Relocated in {info.get('moved_year', 1968)} to escape Lake Nasser flooding
""")
        
        # Current status
        status = self.temple_data.get('current_status', {})
        context_parts.append(f"""
CURRENT STATUS (as of {status.get('last_updated', 'today')}):
- Health Score: {status.get('health_score', 87)}/100
- Risk Level: {status.get('risk_level', 'moderate').upper()}
- Foundation Movement: {status.get('foundation_movement_mm', 0)}mm detected
- Lake Nasser Level: {status.get('water_level_lake_nasser', 175)}m
- Temperature: {status.get('temperature_celsius', 35)}°C
- Daily Visitors: {status.get('daily_visitors', 8500):,}
""")
        
        # NASA Analysis
        if self.nasa_data:
            context_parts.append(f"""
NASA SATELLITE ANALYSIS:
Data Source: {self.nasa_data.get('data_source', 'Sentinel-1 SAR')}
Period: {self.nasa_data.get('analysis_period', '2020-2024')}

Key Findings:
{chr(10).join('- ' + finding for finding in self.nasa_data.get('key_findings', []))}

Current Measurements:
- Latest Displacement: {self.nasa_data.get('current_status', {}).get('latest_displacement_mm', 0):.2f}mm
- Water Level: {self.nasa_data.get('current_status', {}).get('latest_water_level_m', 175):.1f}m
- Displacement Rate: {self.nasa_data.get('current_status', {}).get('displacement_velocity_mm_year', 0):.2f}mm/year
""")
        
        # Threats
        threats = self.temple_data.get('threats', [])
        if threats:
            threat_text = "PRIMARY THREATS:\n"
            for threat in threats:
                threat_text += f"\n- {threat['threat']} ({threat['severity'].upper()})\n"
                threat_text += f"  {threat['description']}\n"
                threat_text += f"  Impact: {threat['impact']}\n"
            context_parts.append(threat_text)
        
        return "\n".join(context_parts)
    
    def get_all_data(self) -> Dict[str, Any]:
        """Get all data combined"""
        return {
            **self.temple_data,
            'nasa_analysis': self.nasa_data
        }