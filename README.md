# Helios Memory Substrate

Helios Memory Substrate is an early-stage Python prototype for a cognitive memory substrate. The long-term goal is to support long-context AI systems, agentic workflows, and large-scale retrieval through tiered memory, ingestion, scoring, persistence, and future distributed coordination.

The current repository contains the foundation only: a validated importance-scoring core, a basic ingestion agent, a production node shell, tests, and CI. Distributed clustering, vector retrieval, persistence, replication, compression, and observability are planned work rather than completed features.

## Vision

Helios is built around one idea:

LLMs need memory systems that behave more like cognition, not just storage.

The substrate is intended for:

- Autonomous agents
- Long-running workflows
- Multi-agent orchestration
- High-volume ingestion pipelines
- Real-time vector retrieval
- Distributed memory clusters

## Current Implementation Status

Implemented:

- `VectorRecord` data model
- Validated importance score calculation
- Basic `QuarkIngestionAgent`
- Basic `HeliosProductionNode`
- Pytest test suite
- GitHub Actions CI workflow

Partially implemented:

- Node status reporting
- Ingestion normalization
- Local storage directory initialization

Planned:

- Persistent storage
- Vector retrieval
- Distributed clustering
- Node-to-node replication
- Memory compression
- Observability and benchmark reporting

## Core Architecture

### 1. Quark Ingestion Layer

Current:

- Normalizes incoming memory text
- Assigns UUIDs
- Adds UTC creation timestamps
- Rejects empty content

Planned:

- Batch ingestion
- Metadata extraction
- Pre-processing for vectorization
- Persistence hooks

### 2. Helios Distributed Core

Current:

- Maintains cluster state placeholder
- Calculates importance scores using similarity, tier, age, and drift factor
- Validates invalid similarity and age values

Planned:

- Cluster-aware memory distribution
- Drift-aware decay refinements
- Tiered memory retention
- Retrieval scoring
- p99/p55 latency tracking

### 3. Production Node Layer

Current:

- Node identity
- Storage path creation
- Node status reporting
- Integration with core and ingestion layer

Planned:

- Health checks
- Persistent node state
- Node-to-node replication
- Observability events

## Installation

```bash
git clone https://github.com/Helios-Memory-System/Helios-Memory-Substrate-1.1.git
cd Helios-Memory-Substrate-1.1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Usage Example

```python
from production_node import HeliosProductionNode

node = HeliosProductionNode(node_id="node-1", storage_path="./data")
print(node.get_status())

record = node.ingestor.ingest("This is a memory object.")
print(record)
```

## Testing

Helios Memory Substrate uses pytest for testing.

Run all tests:

```bash
pytest -v
```

Generate a coverage report:

```bash
pytest --cov=. --cov-report=term-missing
```

Test directory structure:

```text
tests/
├── test_helios_core.py
├── test_production_node.py
└── test_quark_ingest.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

## Security

See [SECURITY.md](SECURITY.md) for vulnerability reporting instructions.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned milestones.

## License

This project is licensed under the **PolyForm Noncommercial License 1.0.0** with the **Commons Clause** condition.

- Non-commercial use such as research, personal projects, education, and open-source experimentation is permitted under the license terms.
- Commercial use, including selling, hosting as a service, or incorporating into a commercial product, is prohibited without a separate commercial license from Travis Papenbrock.

See [LICENSE](LICENSE) for the full terms. To inquire about a commercial license, contact tpapenb@iu.edu.
