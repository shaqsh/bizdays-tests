from http.client import responses

import requests

baseurl = "http://ko85.intabs.net:28080/v1"

def run_core_test(region, date, status_code, response_data=None):

    response = requests.get(baseurl + "/regions/" + region + "/days/" + date)

    assert response.status_code == status_code

    # if status_code == 200:
        # assert response.text.strip() == response_data

    # path http://ko85.intabs.net:28080/v1/regions/{region}/days/{date}
    print("\nRequest: " + str(baseurl) + "/regions/" + str(region) + "/days/" + str(date) + "\nStatus code: " + str(response.status_code) + "\nResponse: " + str(response.text))

# positive tests

def test_current_year_business_day():
    run_core_test("ru", "2024-09-04", 200, "true")

def test_current_year_nonworking_day():
    run_core_test("ru", "2024-05-09", 200, "false")

def test_last_year_business_day():
    run_core_test("ru", "2023-09-06", 200, "true")

def test_last_year_nonworking_day():
    run_core_test("ru", "2023-01-01", 200, "false")

    # This test also covers 'Last year lower boundary' item

def test_next_year_business_day():
    run_core_test("ru", "2025-09-10", 200, "true")

    # This test also covers 'Next year upper boundary' item

def test_next_year_nonworking_day():
    run_core_test("ru", "2025-01-01", 200, "false")

### different date formats

def test_date_format_01():
    run_core_test("ru", "20240904", 200, "true")

def test_date_format_02():
    run_core_test("ru", "04.09.2024", 200, "true")

def test_date_format_03():
    run_core_test("ru", "04-09-2024", 200, "true")

### boundary values tests

def test_year_before_upper_boundary():
    run_core_test("ru", "2023-12-31", 400, "true")
    
def test_year_after_lower_boundary():
    run_core_test("ru", "2026-01-01", 400, "false")

### negative tests

def test_unsupported_region():
    run_core_test("es", "2024-06-15", 400)

def test_unsupported_date_format():
    run_core_test("es", "24.15.06", 400)

def test_empty_date():
    run_core_test("es", "", 404)

def test_text_date():
    run_core_test("es", "bullshit", 400)