CREATE TABLE context_nodes (
    node_id UUID PRIMARY KEY,
    parent_id UUID UNIQUE,
    version_index INTEGER NOT NULL,
    hash_self TEXT NOT NULL,
    hash_parent TEXT,
    raw_payload BYTEA NOT NULL,
    status TEXT CHECK (status IN ('active', 'archived')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_parent FOREIGN KEY (parent_id) REFERENCES context_nodes(node_id)
);

CREATE OR REPLACE FUNCTION protect_immutable_nodes() RETURNS TRIGGER AS $$
BEGIN RAISE EXCEPTION 'Immutability Violation: Registry records are append-only.'; END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_protect_nodes BEFORE UPDATE OR DELETE ON context_nodes FOR EACH ROW EXECUTE FUNCTION protect_immutable_nodes();
CREATE INDEX idx_active_status ON context_nodes (status) WHERE status = 'active';
