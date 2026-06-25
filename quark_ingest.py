from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(frozen=True)
class MemoryRecord:
    id: str
    content: str
    created_at: str


class QuarkIngestionAgent:
    def ingest(self, content: str) -> MemoryRecord:
        if not content or not content.strip():
            raise ValueError("content cannot be empty")

        return MemoryRecord(
            id=str(uuid4()),
            content=content.strip(),
            created_at=datetime.now(timezone.utc).isoformat(),
        )
