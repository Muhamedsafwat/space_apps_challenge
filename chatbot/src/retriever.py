from sentence_transformers import SentenceTransformer, util
import numpy as np
from typing import List, Dict, Any

class SmartRetriever:
    """Semantic search for relevant context"""
    
    def __init__(self, temple_data: Dict[str, Any]):
        print("Loading semantic search model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.chunks = self._build_chunks(temple_data)
        self.embeddings = self.model.encode(
            [c['text'] for c in self.chunks],
            convert_to_tensor=True
        )
        print("✅ Retriever ready")
    
    def _build_chunks(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Build searchable knowledge chunks"""
        chunks = []
        
        # Status
        status = data.get('current_status', {})
        chunks.append({
            'type': 'status',
            'text': f"Temple health: {status.get('health_score')}/100, "
                   f"foundation movement {status.get('foundation_movement_mm')}mm, "
                   f"risk {status.get('risk_level')}, "
                   f"water level {status.get('water_level_lake_nasser')}m"
        })
        
        # Threats
        for threat in data.get('threats', []):
            chunks.append({
                'type': 'threat',
                'text': f"{threat['threat']}: {threat['description']}. "
                       f"Severity: {threat['severity']}. {threat['impact']}"
            })
        
        # NASA findings
        nasa = data.get('nasa_analysis', {})
        for finding in nasa.get('key_findings', []):
            chunks.append({
                'type': 'nasa',
                'text': f"NASA satellite data shows: {finding}"
            })
        
        # History
        for event in data.get('historical_events', []):
            text = f"In {event['year']}: {event['event']}"
            if 'details' in event:
                text += f". {event['details']}"
            chunks.append({
                'type': 'history',
                'text': text
            })
        
        return chunks
    
    def search(self, query: str, top_k: int = 3) -> str:
        """Search and return formatted context"""
        query_emb = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_emb, self.embeddings)[0]
        top_idx = np.argsort(-scores.cpu().numpy())[:top_k]
        
        context_parts = []
        for idx in top_idx:
            if scores[idx] > 0.2:  # Relevance threshold
                chunk = self.chunks[idx]
                context_parts.append(f"[{chunk['type'].upper()}] {chunk['text']}")
        
        return "\n\n".join(context_parts) if context_parts else "No specific relevant data found."