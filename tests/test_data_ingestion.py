import pytest
from src.data_ingestion import aws, azure, gcp, normalizer


def test_fetch_cost_data_shapes():
    aws_data = aws.fetch_cost_data()
    azure_data = azure.fetch_cost_data()
    gcp_data = gcp.fetch_cost_data()
    for data in (aws_data, azure_data, gcp_data):
        assert isinstance(data, list)
        assert all('provider' in r and 'service' in r and 'cost' in r for r in data)


def test_normalize():
    raw = [
        {'provider': 'aws', 'service': 'ec2', 'cost': '10'},
        {'provider': 'gcp', 'service': 'compute', 'cost': 5},
    ]
    norm = normalizer.normalize(raw)
    assert norm == [
        {'provider': 'aws', 'service': 'ec2', 'cost': 10.0},
        {'provider': 'gcp', 'service': 'compute', 'cost': 5.0},
    ]
