'''
Run through terminal
'''


import requests



def run_api_tests(base_url="http://127.0.0.1:8081", detailed=False):
    total_tests = 0
    successful_tests = 0
    print("Running API tests...")


    def test_endpoint(endpoint, method="GET", payload=None):
        nonlocal total_tests, successful_tests
        total_tests += 1

        url = f"{base_url}{endpoint}"
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, json=payload)
        else:
            if detailed:
                print(f"{endpoint} | {method.upper()} | Unsupported method")
            return

        status_code = response.status_code
        test_result = "PASS" if status_code < 400 else "FAIL"
        if test_result == "PASS":
            successful_tests += 1

        if detailed:
            print(f"{endpoint} | {method.upper()} | {status_code} | {test_result}")

    if detailed:
        print("Testing API Endpoints...")

    # --- Words Endpoints ---
    test_endpoint("/api/words")
    # test_endpoint("/api/words/1")
    #
    # # --- Groups Endpoints ---
    # test_endpoint("/api/groups")
    # test_endpoint("/api/groups/1")
    # test_endpoint("/api/groups/1/words")
    # test_endpoint("/api/groups/1/study_sessions")
    #
    # # --- Study Sessions Endpoints ---
    # test_endpoint("/api/study_sessions")
    # test_endpoint("/api/study_sessions/123")
    # test_endpoint("/api/study_sessions/123/words")
    # test_endpoint("/api/study_sessions/123/words/1/review", method="POST", payload={"correct": True})
    #
    # # --- Study Activities Endpoints ---
    # test_endpoint("/api/study_activities/1")
    # test_endpoint("/api/study_activities/1/study_sessions")
    # test_endpoint("/api/study_activities", method="POST", payload={"group_id": 123, "study_activity_id": 456})
    #
    # # --- Dashboard Endpoints ---
    # test_endpoint("/api/dashboard/last_study_session")
    # test_endpoint("/api/dashboard/study_progress")
    # test_endpoint("/api/dashboard/quick-stats")
    #
    # # --- Reset Endpoints ---
    # test_endpoint("/api/reset/reset_history", method="POST")
    # test_endpoint("/api/reset/full_reset", method="POST")
    #
    # # Print overall summary
    # summary = f"Tested {total_tests} endpoints / {successful_tests} passed"
    # print(summary)

if __name__ == "__main__":
    # Pass a custom URL and choose whether to print detailed output or just a summary.
    # For detailed output: run_api_tests("http://127.0.0.1:8081", detailed=True)
    # For summary only: run_api_tests("http://127.0.0.1:8081", detailed=False)
    run_api_tests()