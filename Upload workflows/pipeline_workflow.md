# Automation Workflow

## Pipeline A – Demo Call Processing

Input:
demo transcript (input/demo1.txt)

Steps:
1. extract_demo.py reads the transcript.
2. The script extracts structured information.
3. Structured data is saved as memo.json.
4. generate_agent.py creates the Retell agent configuration.
5. Output saved as agent_spec.json.

Flow:

demo1.txt
   ↓
extract_demo.py
   ↓
memo.json
   ↓
generate_agent.py
   ↓
agent_spec.json


## Pipeline B – Onboarding Update

Input:
onboarding transcript (input/onboarding1.txt)

Steps:
1. update_agent.py reads onboarding information.
2. Updates existing account memo.
3. Saves updated configuration as memo_v2.json.

Flow:

onboarding1.txt
   ↓
update_agent.py
   ↓
memo_v2.json


## Output Location

All outputs are stored in the output folder.
