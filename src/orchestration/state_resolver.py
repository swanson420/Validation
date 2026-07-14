import psycopg2, json
class StateResolver:
    def __init__(self, persistence): self.persistence = persistence
    def get_latest_active_node(self):
        with psycopg2.connect(**self.persistence.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT raw_payload FROM context_nodes WHERE status = 'active' LIMIT 1")
                res = cur.fetchone()
                if not res: raise RuntimeError("No active state.")
                return json.loads(res[0].decode())
