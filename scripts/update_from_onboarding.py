import os
import json

ACCOUNTS_FOLDER = "outputs/accounts"
ONBOARDING_FOLDER = "dataset/onboarding_calls"
CHANGELOG_FOLDER = "changelog"


def extract_updates(text):

    updates = {}

    if "8 AM to 6 PM" in text:
        updates["business_hours"] = {
            "days": "Mon-Fri",
            "start": "08:00",
            "end": "18:00",
            "timezone": "PST"
        }

    if "sprinkler leak" in text:
        updates["emergency_definition"] = [
            "sprinkler leak",
            "fire alarm triggered",
            "water flow alarm"
        ]

    if "Office address" in text:
        updates["office_address"] = "123 Industrial Street, Texas"

    return updates


def update_account(account, updates):

    for key, value in updates.items():
        account[key] = value

    return account


def create_changelog(account_id, updates):

    os.makedirs(CHANGELOG_FOLDER, exist_ok=True)

    log_file = f"{CHANGELOG_FOLDER}/{account_id}.md"

    with open(log_file, "w") as f:

        f.write("# Changes from v1 to v2\n\n")

        for key in updates:
            f.write(f"- Updated {key}\n")


def process_onboarding():

    for account_id in os.listdir(ACCOUNTS_FOLDER):

        v1_path = f"{ACCOUNTS_FOLDER}/{account_id}/v1/account_memo.json"

        if not os.path.exists(v1_path):
            continue

        with open(v1_path) as f:
            account = json.load(f)

        onboarding_file = f"{ONBOARDING_FOLDER}/onboarding1.txt"

        with open(onboarding_file) as f:
            text = f.read()

        updates = extract_updates(text)

        updated_account = update_account(account, updates)

        v2_folder = f"{ACCOUNTS_FOLDER}/{account_id}/v2"

        os.makedirs(v2_folder, exist_ok=True)

        with open(f"{v2_folder}/account_memo.json", "w") as f:
            json.dump(updated_account, f, indent=4)

        create_changelog(account_id, updates)


if __name__ == "__main__":
    process_onboarding()