'''
Run through terminal
'''


import requests

# Set the base URL to where your API is running.
base_url = "http://localhost:5000"

def test_endpoint(endpoint, method="GET", payload=None):
    url = f"{base_url}{endpoint}"
    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, json=payload)
    else:
        print(f"Unsupported method: {method}")
        return

    print(f"Tested endpoint: {endpoint}")
    print("HTTP Method:", method)
    print("Status Code:", response.status_code)
    try:
        json_data = response.json()
        print("Response JSON:", json_data)
    except Exception as e:
        print("Response content:", response.text)
    print("-" * 50)

if __name__ == "__main__":
    print("Testing API Endpoints...")
    # --- Words Endpoints ---
    test_endpoint("/api/words")
    test_endpoint("/api/words/1")

    # --- Groups Endpoints ---
    test_endpoint("/api/groups")
    test_endpoint("/api/groups/1")
    test_endpoint("/api/groups/1/words")
    test_endpoint("/api/groups/1/study_sessions")

    # --- Study Sessions Endpoints ---
    test_endpoint("/api/study_sessions")
    test_endpoint("/api/study_sessions/123")
    test_endpoint("/api/study_sessions/123/words")
    test_endpoint("/api/study_sessions/123/words/1/review", method="POST", payload={"correct": True})

    # --- Study Activities Endpoints ---
    test_endpoint("/api/study_activities/1")
    test_endpoint("/api/study_activities/1/study_sessions")
    test_endpoint("/api/study_activities", method="POST", payload={"group_id": 123, "study_activity_id": 456})

    # --- Dashboard Endpoints ---
    test_endpoint("/api/dashboard/last_study_session")
    test_endpoint("/api/dashboard/study_progress")
    test_endpoint("/api/dashboard/quick-stats")

    # --- Reset Endpoints ---
    test_endpoint("/api/reset/reset_history", method="POST")
    test_endpoint("/api/reset/full_reset", method="POST")

    print("Testing Complete.")