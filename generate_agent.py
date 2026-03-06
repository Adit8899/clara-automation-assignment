import json

# load memo data
with open("output/memo.json", "r") as f:
    memo = json.load(f)

# create agent configuration
agent = {
    "agent_name": memo["company_name"] + " Support Agent",
    "voice_style": "professional",
    "version": "v1",
    "system_prompt": f"""
You are a helpful phone assistant for {memo["company_name"]}.

Business Hours Flow:
- greet the caller
- ask the reason for calling
- collect caller name and phone number
- route the call appropriately
- if transfer fails apologize and take message
- ask if anything else is needed
- close call

After Hours Flow:
- greet caller
- ask purpose
- confirm if emergency
- if emergency collect name, phone, and address
- attempt transfer to emergency dispatch
- if transfer fails reassure caller and promise follow-up
"""
}

# save agent configuration
with open("output/agent_spec.json", "w") as f:
    json.dump(agent, f, indent=2)

print("agent_spec.json created successfully")