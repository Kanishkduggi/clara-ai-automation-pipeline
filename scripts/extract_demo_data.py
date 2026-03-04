import os
import json
import uuid

INPUT_FOLDER = "dataset/demo_calls"
OUTPUT_FOLDER = "outputs/accounts"

def extract_information(text):

    data = {
        "account_id": str(uuid.uuid4()),
        "company_name": "",
        "business_hours": {},
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": {},
        "non_emergency_routing_rules": {},
        "call_transfer_rules": {},
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    return data


def process_demo_calls():

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for file in os.listdir(INPUT_FOLDER):

        if file.endswith(".txt"):

            with open(f"{INPUT_FOLDER}/{file}", "r") as f:
                transcript = f.read()

            account_data = extract_information(transcript)

            account_id = account_data["account_id"]

            account_folder = f"{OUTPUT_FOLDER}/{account_id}/v1"

            os.makedirs(account_folder, exist_ok=True)

            with open(f"{account_folder}/account_memo.json", "w") as f:
                json.dump(account_data, f, indent=4)


if __name__ == "__main__":
    process_demo_calls()