"""Entry point for the Cost Optimization Toolkit."""
from data_ingestion import aws, azure, gcp, normalizer
from cost_analysis import (
    cost_breakdown,
    optimization_recommendations,
    reserved_instance,
    budget_tracking,
)
from automation import report_generator, notifier
from advanced import ml_prediction, anomaly_detection
from config.config import config
from utils.logger import get_logger


logger = get_logger(__name__)


def run() -> None:
    logger.info("Fetching cost data")
    data = aws.fetch_cost_data() + azure.fetch_cost_data() + gcp.fetch_cost_data()
    norm = normalizer.normalize(data)

    breakdown = cost_breakdown.by_provider(norm)
    recommendations = optimization_recommendations.find_underutilized(norm)
    ri = reserved_instance.recommend_reserved(norm)
    recommendations.extend(ri)
    anomalies = anomaly_detection.detect_anomalies(norm)
    recommendations.extend(anomalies)

    total = budget_tracking.total_cost(norm)
    over_budget = budget_tracking.is_over_budget(total, config.budget_limit)

    predicted = ml_prediction.predict_next_month(norm)
    logger.info("Predicted next month cost: %.2f", predicted)

    report = report_generator.generate(breakdown, recommendations)
    notifier.notify(report)
    if over_budget:
        notifier.notify("Budget limit exceeded!", channel="alert")


if __name__ == "__main__":
    run()
