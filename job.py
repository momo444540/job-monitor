name: Run Python Job

on:
  workflow_dispatch:

jobs:
  run-job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install requests
          pip install beautifulsoup4

      - name: Run script
        run: python job.py
