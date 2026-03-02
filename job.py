name: Job Monitor

on:
  schedule:
    - cron: '0 1 * * *'
  workflow_dispatch:

jobs:
  monitor:
    runs-on: ubuntu-latest

    steps:
      - name: 拉取代码
        uses: actions/checkout@v3

      - name: 安装 Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: 安装依赖
        run: |
          pip install requests beautifulsoup4

      - name: 运行 Python
        id: check
        run: |
          RESULT=$(python job.py)
          echo "$RESULT"
          echo "result<<EOF" >> $GITHUB_OUTPUT
          echo "$RESULT" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: 发送通知
        if: contains(steps.check.outputs.result, 'DATA_CHANGED')
        run: |
          echo "发现新岗位："
          echo "${{ steps.check.outputs.result }}"
