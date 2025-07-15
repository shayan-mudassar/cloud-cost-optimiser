# Running the Cost Optimization Toolkit

This guide provides a quick overview on how to start each component of the project and how to run the tests.

## Prerequisites
- Python 3.8+
- Node.js 14+
- `pip` and `npm` available in your `PATH`

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Install Node.js dependencies for the dashboard server:
```bash
npm install
```

## Running the Backend
The backend is a simple Node.js server serving a placeholder dashboard. Start it with:
```bash
npm start
```
By default the server listens on port `3000`.

## Running the ML and Automation Pipeline
The main entry point for the Python modules is `src/main.py`. It fetches mock cost data, performs analysis and sends a notification:
```bash
python -m src.main
```

## Running the Tests
Tests are written with `pytest`. After installing the Python dependencies you can run all tests with:
```bash
pytest
```

