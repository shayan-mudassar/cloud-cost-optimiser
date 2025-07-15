from src.advanced import ml_prediction, anomaly_detection, gamification, rules_engine


def test_ml_prediction():
    records = [{'cost': 10}, {'cost': 30}]
    assert ml_prediction.predict_next_month(records) == 20


def test_anomaly_detection():
    records = [{'provider': 'aws', 'service': 'ec2', 'cost': 250}]
    alerts = anomaly_detection.detect_anomalies(records)
    assert any('Anomaly detected' in a for a in alerts)


def test_gamification():
    assert gamification.score_actions(['a', 'b']) == 20


def test_rules_engine():
    rules = [lambda r: r.get('cost', 0) > 5]
    records = [{'cost': 10}, {'cost': 2}]
    matched = rules_engine.apply_rules(records, rules)
    assert matched == [{'cost': 10}]
