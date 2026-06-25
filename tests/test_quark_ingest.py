import pytest

from quark_ingest import QuarkIngestionAgent, MemoryRecord


def test_ingest_returns_memory_record():
    agent = QuarkIngestionAgent()

    record = agent.ingest("sample content")

    assert isinstance(record, MemoryRecord)
    assert record.content == "sample content"
    assert record.id
    assert record.created_at


def test_ingest_rejects_empty_content():
    agent = QuarkIngestionAgent()

    with pytest.raises(ValueError):
        agent.ingest("   ")
