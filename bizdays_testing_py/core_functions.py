import requests

baseurl = "http://ko85.intabs.net:28080/v1"

def run_test(region, date, status_code, headers_set={'Accept': 'text/plain'}, response_plain=None, response_json_type=None):

    request_full = str(baseurl + "/regions/" + region + "/days/" + date)
    response = requests.get(request_full, headers=headers_set)
    #response = requests.get(baseurl + "/regions/" + region + "/days/" + date, headers=headers_set)

    #assert response.status_code == status_code

    if status_code == 200:

        if headers_set == {'Accept': 'application/json'}:

            print("\nIt's JSON")
            print("Date: " + response.json()['date'])
            print("Type: " + response.json()['type'])

            assert response.json()['date'] == date
            assert response.json()['type'] == response_json_type

        else:

            assert response.text.strip() == response_plain


    # path http://ko85.intabs.net:28080/v1/regions/{region}/days/{date}
    print("\nRequest: " + str(request_full) + "\nStatus code: " + str(response.status_code) + "\nResponse raw: " + str(response.text))

def run_test_offset(region, date, status_code, date_offset, headers_set={'Accept': 'text/plain'}, response_plain=None, response_json_endDate=None, response_json_distance=None):

    request_offset_full = str(baseurl + "/regions/" + region + "/days/" + date + "/offset/" + date_offset)
    response_offset = requests.get(request_offset_full, headers=headers_set)

    assert  response_offset.status_code == status_code

    print("\nRequest: " + str(request_offset_full) + "\nStatus code: " + str(response_offset.status_code) + "\nResponse raw: " + str(response_offset.text))