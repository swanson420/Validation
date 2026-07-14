from src.engine.node_builder import create_node
from src.engine.validation_service import verify_lineage

class StateTransitionOrchestrator:
    def __init__(self, persistence): self.persistence = persistence
    def process_proposal(self, payload, last_node):
        new_node = create_node(payload, last_node)
        verify_lineage(new_node, last_node)
        self.persistence.insert_node(new_node)
        return new_node
