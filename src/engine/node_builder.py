import uuid
from datetime import datetime, timezone
from typing import Dict, Any, Optional
from src.engine.crypto_engine import generate_self_hash

def create_node(payload: Dict[str, Any], parent_node: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    version_index = (parent_node['version_index'] + 1) if parent_node else 0
    parent_id = parent_node['node_id'] if parent_node else None
    timestamp = datetime.now(timezone.utc).isoformat()
    node_id = str(uuid.uuid4())
    hash_self = generate_self_hash(payload, parent_id, version_index, timestamp)
    return {
        "node_id": node_id, "parent_id": parent_id, "version_index": version_index,
        "payload": payload, "hash_self": hash_self, "hash_parent": parent_node['hash_self'] if parent_node else None,
        "status": "active", "created_at": timestamp
    }
