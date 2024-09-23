from core_functions import run_test_offset

def test_offset_future():
    run_test_offset("ru", "2024-09-23", 200, "2", None, None)

def test_offset_past():
    run_test_offset("ru", "2024-09-23", 200, "-4", None, None)