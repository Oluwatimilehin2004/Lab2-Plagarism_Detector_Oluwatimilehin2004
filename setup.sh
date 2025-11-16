#!/bin/bash

# setup.sh - Project Setup Script
# Creates essays and reports directories, and logs the setup process

chmod u+x setup.sh
LOG_FILE="setup.log"

# Start logging
echo "---- Project Setup Started: $(date) ----" >> "$LOG_FILE"

# Create essays folder
if [ ! -d "essays" ]; then
  mkdir essays
  echo "Created 'essays' directory." >> "$LOG_FILE"
else
  echo "'essays' directory already exists." >> "$LOG_FILE"
fi

# Create reports folder
if [ ! -d "reports" ]; then
  mkdir reports
  echo "Created 'reports' directory." >> "$LOG_FILE"
else
  echo "'reports' directory already exists." >> "$LOG_FILE"
fi

# Completion log
echo "---- Setup Completed Successfully: $(date) ----" >> "$LOG_FILE"
echo "Project setup done! Logs saved to setup.log"

