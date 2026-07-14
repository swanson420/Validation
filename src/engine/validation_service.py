from typing import Dict, Any, Optional

class IntegrityError(Exception): pass

def verify_lineage(node: Dict[str, Any], parent_node: Optional[Dict[str, Any]]) -> bool:
    if parent_node and node['hash_parent'] != parent_node['hash_self']:
        raise IntegrityError("Hash mismatch: Lineage broken.")
    if parent_node and parent_node['status'] != 'active':
        raise IntegrityError("Parent node must be 'active'.")
    return True
