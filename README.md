# Clara Answers Automation Assignment

## Overview
This project builds a zero-cost automation pipeline that converts demo call transcripts into structured account data and generates a Retell agent configuration.

## Pipeline A – Demo Call
Demo transcript → memo.json → agent_spec.json

Steps:
1. Read transcript from input/demo1.txt
2. Extract structured information
3. Save structured data in output/memo.json
4. Generate Retell agent configuration in output/agent_spec.json

## Pipeline B – Onboarding Update
Onboarding transcript → memo_v2.json

Steps:
1. Read onboarding transcript
2. Update existing account configuration
3. Save updated data in memo_v2.json

## Tools Used
- Python
- JSON files
- Visual Studio Code

## How to Run

Run the following commands:

python scripts/extract_demo.py

python scripts/generate_agent.py

python scripts/update_agent.py

## Output Files

output/
- memo.json
- agent_spec.json
- memo_v2.json

## Version Tracking
Changes between versions are recorded in the changelog folder.