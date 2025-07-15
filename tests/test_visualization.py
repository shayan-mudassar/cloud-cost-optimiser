from pathlib import Path


def test_dashboard_server_exists():
    path = Path('src/visualization/dashboard/server.js')
    assert path.exists()
