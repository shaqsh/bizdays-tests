from core_functions import run_test_offset


### POSITIVE TESTS


def test_offset_forward():
    run_test_offset("ru", "2024-09-23", 200, "46", None, "2024-11-27")

def test_offset_backward():
    run_test_offset("ru", "2024-09-23", 200, "-23", None, "2024-08-21")

def test_offset_null():
    run_test_offset("ru", "2024-09-23", 200, "0", None, "2024-09-23")


### POSITIVE, ACCEPT JSON


def test_offset_forward_json():
    run_test_offset("ru", "2024-09-23", 200, "2", {'Accept': 'application/json'}, None, "2024-09-25", 2)

def test_offset_backward_json():
    run_test_offset("ru", "2024-09-23", 200, "-4", {'Accept': 'application/json'}, None, "2024-09-17", -4)


### NEGATIVE TESTS


def test_offset_outside_range_forward():
    run_test_offset("ru", "2024-09-23", 400, "6000000")

def test_offset_outside_range_backward():
    run_test_offset("ru", "2024-09-23", 400, "-6000000")

def test_offset_incorrect_data():
    run_test_offset("ru", "2024-09-23", 400, "six gorillion")

def test_offset_empty():
    run_test_offset("ru", "2024-09-23", 404, "")