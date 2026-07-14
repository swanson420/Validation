import psycopg2, json
from psycopg2 import errors

class IntegrityError(Exception): pass

class ContextPersistence:
    def __init__(self, db_config: dict): self.conn_params = db_config
    def insert_node(self, node: dict):
        try:
            with psycopg2.connect(**self.conn_params) as conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO context_nodes VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                                (node['node_id'], node['parent_id'], node['version_index'], node['hash_self'], 
                                 node['hash_parent'], json.dumps(node).encode(), node['status'], node['created_at']))
                    conn.commit()
        except errors.UniqueViolation: raise IntegrityError("Concurrency conflict.")
