from core_functions import run_test_business


### POSITIVE TESTS


def test_current_year_business_day():
    run_test_business("ru", "2024-09-04", 200, None, "true")

def test_current_year_nonworking_day():
    run_test_business("ru", "2024-05-09", 200, None, "false")

def test_last_year_business_day():
    run_test_business("ru", "2023-09-06", 200, None, "true")

def test_last_year_nonworking_day():
    run_test_business("ru", "2023-01-01", 200, None, "false")

def test_next_year_business_day():
    run_test_business("ru", "2025-09-10", 200, None, "true")

def test_next_year_nonworking_day():
    run_test_business("ru", "2025-01-01", 200, None, "false")


### POSITIVE, ACCEPT JSON


def test_current_year_business_day_json():
    run_test_business("ru", "2024-09-04", 200, {'Accept': 'application/json'}, None, "business")


def test_current_year_nonworking_day_json():
    run_test_business("ru", "2024-05-09", 200, {'Accept': 'application/json'}, None, "non-business")


### POSITIVE, CONTENT NEGOTIATION


def test_content_negotiation():
    run_test_business("ru", "2024-05-09", 200, {'Accept': 'application/json,text/plain;q=1'}, "false")


### POSITIVE, DIFFERENT DATE FORMATS


def test_date_format_01():
    run_test_business("ru", "20240904", 200, None, "true")

def test_date_format_02():
    run_test_business("ru", "04.09.2024", 200, None, "true")

def test_date_format_03():
    run_test_business("ru", "04-09-2024", 200, None, "true")


### NEGATIVE TESTS


def test_outside_range_past():
    run_test_business("ru", "1866-09-21", 400)

def test_outside_range_future():
    run_test_business("ru", "802701-09-23", 400)

def test_unsupported_region():
    run_test_business("es", "2024-06-15", 400)

def test_unsupported_date_format():
    run_test_business("ru", "24.15.06", 400)

def test_empty_date():
    run_test_business("ru", "", 404)

def test_text_date():
    run_test_business("ru", "bullshit", 400)


### NEGATIVE, HEADERS


def test_unsupported_mime():
    run_test_business("ru", "2024-09-04", 406, {'Accept': 'text/pdf'})

def test_incorrect_mime():
    run_test_business("ru", "2024-05-09", 406, {'Accept': 'bullshit12345'})