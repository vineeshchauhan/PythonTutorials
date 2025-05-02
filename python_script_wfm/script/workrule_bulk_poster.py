import requests
import json
import time

# CONFIGURATION
WORK_RULE_NAMES_FILE = "../work_rule_name.txt"
WORK_SAMPLE_PAYLOAD_FILE = "../work_rule_sample.json"
ENDPOINT_URL = "https://{{end-point}}/api/v1/timekeeping/setup/full_work_rules"
# If authentication is needed, set your token here
AUTH_TOKEN = "Bearer AUTH_TOKEN"

def load_payrule_names(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def load_sample_payload(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def post_payrule(payload, endpoint, auth_token=None):
    headers = {"Content-Type": "application/json"}
    if auth_token:
        headers["Authorization"] = auth_token
    response = requests.post(endpoint, headers=headers, json=payload)
    return response

def main():
    workrule_names = load_payrule_names(WORK_RULE_NAMES_FILE)
    workrule_sample_payload = load_sample_payload(WORK_SAMPLE_PAYLOAD_FILE)

    for idx, name in enumerate(workrule_names, 1):
        payload = json.loads(json.dumps(workrule_sample_payload))  # Deep copy
       # print(json.dumps(payload, indent=2))
        # Set the payrule name (adjust path if nested)
        if "name" in payload :
            payload["name"] = name
        else:
            print(f"ERROR: 'name' key not found or not a dict in sample payload.")
            continue

        print(f"[{idx}/{len(workrule_names)}] Posting payrule: {name}")
        try:
            resp = post_payrule(payload, ENDPOINT_URL, AUTH_TOKEN)
            print(f"  Status: {resp.status_code} | Response: {resp.text[:200]}")
        except Exception as e:
            print(f"  ERROR posting {name}: {e}")

        time.sleep(0.2)  # Be nice to the server

if __name__ == "__main__":
    main()
