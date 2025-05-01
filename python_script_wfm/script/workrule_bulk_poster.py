import requests
import json
import time

# CONFIGURATION
WORK_RULE_NAMES_FILE = "../work_rule_name.txt"
WORK_SAMPLE_PAYLOAD_FILE = "../work_rule_sample.json"
ENDPOINT_URL = "https://Navigator-Test3.evl.mykronos.com/api/v1/timekeeping/setup/full_work_rules"
# If authentication is needed, set your token here
AUTH_TOKEN = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBxQThsQnRiVnZfd195OE9IQkJWeiJ9.eyJuYW1lIjoic3VzZXIiLCJnaXZlbl9uYW1lIjoidXNlciIsImZhbWlseV9uYW1lIjoibmF2aWdhdG9yIiwiZW1haWwiOiJyaXRhLnNpbGl2ZW5AYXR0Lm5ldCIsInVzZXJuYW1lIjoic3VzZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzdXNlciIsInVrZ19wcmVmZXJyZWRfbGFuZ3VhZ2UiOiJlbi1VUyIsInRpZCI6Im9yZ19vQkxQaW14RldiaFFHdTBIIiwidGEiOiJpbnRlcm5hbGRtbXRlY2hub2xvZ3lfdWF0MDMiLCJnbG9iYWxfdGVuYW50X2lkIjoiYTJkZGEwYWEtYzZlZC00YTBiLTk0MTgtYzgzNmE1ZDNiMTM0IiwiaXNzIjoiaHR0cHM6Ly93ZWxjb21lLWV2YWwudWtnLm5ldC8iLCJzdWIiOiJhdXRoMHxmMmIyNGYxNC1jMTJkLTQzMzktYjRmYi1kZjRkZjM4MTZkZjIiLCJhdWQiOlsiaHR0cHM6Ly93Zm0udWtnLm5ldC9hcGkiLCJodHRwczovL3dlbGNvbWUtZXZhbC51a2ctZXZhbC5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzQ2MDM2NjYxLCJleHAiOjE3NDYwMzg0NjEsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIHJlYWQ6dXNlcmluZm8gcHJvZmlsZSBlbWFpbCBhY2Nlc3M6d2ZtIiwiZ3R5IjoicGFzc3dvcmQiLCJhenAiOiIzYTRlZTdiZC1mMGM5LTQwYmMtODViOS03ZDA4MmVmNGI1M2IifQ.oj67kgfeJWVGFX63TcdgnjQFDOiyBaCtGHpR0avRo6634Qhn-0l5wbHd9CITFMev9jY9VvAqEO_YElhfob-UjWbTQcs_PJ5Sge3Teur1GaClkzVmyIwSbJRmNFqopxwmGpJDmWSpwLfoGBgbd3aTB7d-DWkwPC1IXCg-Nm5foUci0q87HiKsALxK6Xlq3jnv5o8XoD8hGgzkMLgPqF4jkDLelmHeWPH1o_Tehs42Z5HYvrBiX81AaGhQiFu69bnkZ71-tTEi6zZdhfqp7APlU-8IJSZHNEa-TVYdWUt59wJ6n_A5vuUnepzYKaicEA_VY1sppHSypbTBuBcwdUw3QA"

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