import json

# load previous memo
with open("output/memo.json", "r") as f:
    memo = json.load(f)

# simulate onboarding updates
memo["business_hours"] = "Mon-Fri 8AM-6PM"

memo["emergency_definition"].append("pipe burst")

# save updated version
with open("output/memo_v2.json", "w") as f:
    json.dump(memo, f, indent=2)

print("memo_v2.json created successfully")