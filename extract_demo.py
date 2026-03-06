import json

# Read the transcript file
with open("input/demo1.txt", "r") as f:
    transcript = f.read().lower()

# Create structured memo data
memo = {
    "account_id": "001",
    "company_name": "ABC Fire Protection",
    "business_hours": "Mon-Fri 9AM-5PM",
    "services_supported": [],
    "emergency_definition": [],
    "questions_or_unknowns": []
}

# Extract services
if "sprinkler" in transcript:
    memo["services_supported"].append("sprinkler repair")

if "fire alarm" in transcript:
    memo["services_supported"].append("fire alarm inspection")

# Define emergency conditions
memo["emergency_definition"] = [
    "sprinkler leak",
    "fire alarm triggered"
]

# Save the JSON output
with open("output/memo.json", "w") as f:
    json.dump(memo, f, indent=2)

print("memo.json created successfully")