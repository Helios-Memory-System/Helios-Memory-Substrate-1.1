from production_node import HeliosProductionNode


def test_production_node_status(tmp_path):
    node = HeliosProductionNode(node_id="node-1", storage_path=str(tmp_path))

    status = node.get_status()

    assert status["node_id"] == "node-1"
    assert status["status"] == "ACTIVE"
    assert status["storage_exists"] is True


def test_production_node_trims_node_id(tmp_path):
    node = HeliosProductionNode(node_id="  node-2  ", storage_path=str(tmp_path))

    assert node.node_id == "node-2"
