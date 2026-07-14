from src.persistence.context_persistence import ContextPersistence
from src.orchestration.state_orchestrator import StateTransitionOrchestrator
from src.orchestration.state_resolver import StateResolver

def assemble_pipeline():
    persistence = ContextPersistence({"dbname": "context_db", "user": "admin"})
    return StateTransitionOrchestrator(persistence), StateResolver(persistence)
