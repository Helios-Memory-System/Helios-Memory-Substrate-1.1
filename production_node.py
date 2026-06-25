from pathlib import Path

from helios_core import HeliosDistributedCore
from quark_ingest import QuarkIngestionAgent


class HeliosProductionNode:
    """Production node shell for local Helios memory operations."""

    def __init__(self, node_id: str, storage_path: str):
        if not node_id or not node_id.strip():
            raise ValueError("node_id cannot be empty")

        self.node_id = node_id.strip()
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.core = HeliosDistributedCore()
        self.ingestor = QuarkIngestionAgent()

    def get_status(self) -> dict:
        return {
            "node_id": self.node_id,
            "status": "ACTIVE",
            "storage": str(self.storage_path),
            "storage_exists": self.storage_path.exists(),
        }


if __name__ == "__main__":
    node = HeliosProductionNode(node_id="node-01", storage_path="./data")
    print(f"Helios Node {node.node_id} is now running.")
