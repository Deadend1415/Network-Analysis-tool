#!/bin/bash

# Absolute path to your Python script
SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/ping_tool.py"
ERROR_LOG="$(cd "$(dirname "$0")" && pwd)/ping_error.log"
PYTHON_BIN=$(which python3)  # Path to Python3 interpreter

# Cron job: run every hour
CRON_JOB="0 * * * * $PYTHON_BIN $SCRIPT_PATH >> $SCRIPT_PATH.log 2>&1"

# Check if cron job already exists
(crontab -l 2>/dev/null | grep -F "$SCRIPT_PATH") && {
    echo "Cron job already exists."
    exit 0
}

# Add new cron job
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
echo "Cron job installed:"
echo "$CRON_JOB"
