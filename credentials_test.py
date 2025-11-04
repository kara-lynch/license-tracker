from src.credentials.credentials_manager import *

def main():
    test_data = [
        { #test 1
            "id": 263,
            "fName": "Aveline'); DROP TABLE Employee; --",
            "lName": "Fishbie",
            "loc": "Japan",
            "dept": "Legal",
            "title": "Manager"
        },
        { #test 2
            "id": 264,
            "fName": "Amélie",
            "lName": "Garçon-Beaumont",
            "loc": "Germany",
            "dept": "Sales",
            "title": "Sales Agent"
        },
        { #test 3
            "id": 265,
            "fName": "Jens",
            "lName": "van der Meer",
            "loc": "Germany",
            "dept": "Information Technology",
            "title": "Developer"
        },
        {}, #test 4
        { #test 5
            "id": 266,
            "first_name": "Kara",
            "lName": "Lynch",
            "loc": "United States",
            "dept": "Information Technology",
            "title": "Developer"
        },
        { #test 6
            "id": 267,
            "fName": "Noelle",
            "lName": "Stark",
            "loc": "United States",
            "dept": "Information Technology"
        }
    ]
    users = []
    test_count = 0
    for test in test_data:
        test_count += 1
        try:
            new_user = UserCredentials(test)
            new_user.validate()
            users.append(new_user)
            print(f"{new_user.name()} added successfully")
        except Exception as e:
            print(f"Test {test_count} failed for reason: {e.args[0]}")

    print("List of users:")
    for user in users:
        print(user.name())

main()