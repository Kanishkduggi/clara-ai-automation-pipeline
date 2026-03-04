import os
import json

ACCOUNTS_FOLDER = "outputs/accounts"


def create_agent_spec(account, version):

    agent = {
        "agent_name": f"{account.get('company_name','Service')} AI Agent",

        "voice_style": "professional",

        "version": version,

        "system_prompt": f"""
You are a voice assistant for {account.get('company_name','a service company')}.

Business Hours Flow:
1. Greet the caller.
2. Ask the reason for the call.
3. Collect caller name and phone number.
4. Route or transfer the call.
5. If transfer fails, apologize and assure follow-up.
6. Ask if they need anything else.
7. Close the call politely.

After Hours Flow:
1. Greet the caller.
2. Ask the reason for the call.
3. Determine if it is an emergency.

Emergency definition:
{account.get("emergency_definition", [])}

If emergency:
- collect name
- collect phone number
- collect address immediately
- attempt transfer

If transfer fails:
- apologize
- assure quick follow up

If non emergency:
- collect details
- inform follow up during business hours
""",

        "key_variables": {
            "business_hours": account.get("business_hours", {}),
            "office_address": account.get("office_address", ""),
            "services_supported": account.get("services_supported", [])
        },

        "call_transfer_protocol": {
            "attempt_transfer": True,
            "timeout_seconds": 60,
            "retry_attempts": 1
        },

        "fallback_protocol": "If transfer fails, collect caller details and inform dispatch team."
    }

    return agent


def generate_specs():

    for account_id in os.listdir(ACCOUNTS_FOLDER):

        account_path = f"{ACCOUNTS_FOLDER}/{account_id}"

        # Check both versions
        for version in ["v1", "v2"]:

            memo_path = f"{account_path}/{version}/account_memo.json"

            if not os.path.exists(memo_path):
                continue

            with open(memo_path, "r") as f:
                account = json.load(f)

            agent = create_agent_spec(account, version)

            output_path = f"{account_path}/{version}/agent_spec.json"

            with open(output_path, "w") as f:
                json.dump(agent, f, indent=4)


if __name__ == "__main__":
    generate_specs()