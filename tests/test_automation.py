from src.automation import report_generator, notifier


def test_report_generator(capsys):
    breakdown = {'aws': 100}
    report = report_generator.generate(breakdown, ['optimize'])
    assert 'Cost Report:' in report
    assert '- aws: $100.00' in report


def test_notifier_logs(caplog):
    with caplog.at_level('INFO'):
        notifier.notify('msg')
    assert 'msg' in caplog.text
