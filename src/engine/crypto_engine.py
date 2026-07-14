import hashlib
import json
from typing import Dict, Any, Optional

def generate_self_hash(payload: Dict[str, Any], parent_id: Optional[str], 
                       version_index: int, timestamp: str) -> str:
    data = {"payload": payload, "parent_id": parent_id, "version_index": version_index, "timestamp": timestamp}
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
