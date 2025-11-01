import requests
import json

API_URL = "http://127.0.0.1:5000/addLicense/"

TEST_BODY = {
    "licenseName": "Windows 10",
    "ver": "10.9.83",
    "type": "Enterprise"
}

# Test 1: Sending a valid token.
def test1() -> bool:
    print("TEST 1: Valid token.")
    valid_token = "eyJhbGciOiJIUzI1NiJ9.eyJsYXN0X25hbWUiOiJGaWxpcGN6eW5za2kiLCJsb2NhdGlvbiI6Ikdlcm1hbnkiLCJpZCI6MTksImRlcGFydG1lbnQiOiJJbmZvcm1hdGlvbiBUZWNobm9sb2d5IiwidGl0bGUiOiJEZXZlbG9wZXIiLCJmaXJzdF9uYW1lIjoiTWFyZ2l0Iiwic3ViIjoiTWFyZ2l0IEZpbGlwY3p5bnNraSIsImlhdCI6MTc2MTk0MTM0MiwiZXhwIjoxNzYxOTQ0OTQyfQ.Amxnx-uGkdrTGdNQjnJ6oSDHldR0iJrQMKLdinyUnRE"

    valid_response = requests.post(API_URL, headers={"Bearer": valid_token}, json=TEST_BODY)
    if valid_response.status_code == 200:
        print("TEST SUCCEEDED")
        # print(json.dumps(json.loads(valid_response.text), indent=4))
        print(valid_response.text)
    else:
        print("ERROR: TEST 1 FAILED!")
        print(valid_response.text)
        print(valid_response.status_code)


# Test 2: Sending an expired token. Token is from 10/29
def test2() -> bool:
    print("TEST 2: Sending a token that is expired.")
    expired_token = "eyJhbGciOiJIUzI1NiJ9.eyJsYXN0X25hbWUiOiJGdXJwaHkiLCJsb2NhdGlvbiI6IkJyYXppbCIsImlkIjoxMywiZGVwYXJ0bWVudCI6IkxlZ2FsIiwidGl0bGUiOiJBaWRlIiwiZmlyc3RfbmFtZSI6IlRoZW9kb3JhIiwic3ViIjoiVGhlb2RvcmEgRnVycGh5IiwiaWF0IjoxNzYxNzc2MzIzLCJleHAiOjE3NjE3Nzk5MjN9.rydmmASGiVMB2pCTuqTxJ5OLqwIEmZfeuIIZceapGMU"

    expired_response = requests.post(API_URL, headers={"Bearer": expired_token}, json=TEST_BODY)
    if expired_response.status_code == 401:
        print("TEST SUCCEEDED")
    else:
        print("TEST FAILED")
        print(expired_response.text)
        print(expired_response.status_code)


# Test 3: Sending a fake token that is too long. (>400 chars)
def test3() -> bool:
    print("TEST 3: Sending a token that is too long.")
    long_token = ""
    for i in range(81):
        long_token += "AAAAA"
    print(f'Length of long token: {len(long_token)}')

    long_response = requests.post(API_URL, headers={"Bearer": long_token}, json=TEST_BODY)
    if long_response.status_code == 401:
        print("TEST SUCCEEDED")
    else:
        print("TEST FAILED")
        print(long_response.text)
        print(long_response.status_code)


# Test 4: Sending a fake token that is too short. (<250 chars)
def test4() -> bool:
    print("TEST 4: Sending a token that is too short.")
    short_token = ""
    for i in range(10):
        short_token += "AAAAA"
    print(f'Length of long token: {len(short_token)}')

    short_response = requests.post(API_URL, headers={"Bearer": short_token}, json=TEST_BODY)
    if short_response.status_code == 401:
        print("TEST SUCCEEDED")
    else:
        print("TEST FAILED")
        print(short_response.text)
        print(short_response.status_code)


# Test 5: Sending empty token.
def test5() -> bool:
    print("TEST 5: Sending empty with request.")
    empty_token = ""

    empty_response = requests.post(API_URL, headers={"Bearer": empty_token}, json=TEST_BODY)
    if empty_response.status_code == 401:
        print("TEST SUCCEEDED")
    else:
        print("TEST FAILED")
        print(empty_response.text)
        print(empty_response.status_code)


# Test 6: Sending no Bearer header along with request.
def test6() -> bool:
    print("Sending no Bearer header along with request.")
    no_token_response = requests.post(API_URL, json=TEST_BODY)
    if no_token_response.status_code == 401:
        print("TEST SUCCEEDED")
    else:
        print("TEST FAILED")
        print(no_token_response.text)
        print(no_token_response.status_code)


if __name__ == "__main__":
    # Test 1: Sending a valid token.
    test1()
    print("\n")

    # Test 2: Sending an expired token. Token is from 10/29
    test2()
    print("\n")

    # Test 3: Sending a fake token that is too long. (>400 chars)
    test3()
    print("\n")

    # Test 4: Sending a fake token that is too short. (<250 chars)
    test4()
    print("\n")

    # Test 5: Sending empty token.
    test5()
    print("\n")

    # Test 6: Sending no Bearer header along with request.
    test6()
    print("\n")