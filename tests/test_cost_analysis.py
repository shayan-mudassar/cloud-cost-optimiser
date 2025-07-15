from src.cost_analysis import cost_breakdown, optimization_recommendations, reserved_instance, budget_tracking


def sample_records():
    return [
        {'provider': 'aws', 'service': 'ec2', 'cost': 120},
        {'provider': 'aws', 'service': 's3', 'cost': 30},
        {'provider': 'gcp', 'service': 'compute', 'cost': 60},
    ]


def test_cost_breakdown():
    bd = cost_breakdown.by_provider(sample_records())
    assert bd == {'aws': 150, 'gcp': 60}


def test_optimization_recommendations():
    recs = optimization_recommendations.find_underutilized(sample_records(), threshold=50)
    assert 'Consider downsizing aws s3' in recs
    assert all('Consider downsizing' in r for r in recs)


def test_reserved_instance():
    sugg = reserved_instance.recommend_reserved(sample_records())
    assert 'Purchase reserved instance for aws ec2' in sugg


def test_budget_tracking():
    total = budget_tracking.total_cost(sample_records())
    assert total == 210
    assert budget_tracking.is_over_budget(total, 200) is True
