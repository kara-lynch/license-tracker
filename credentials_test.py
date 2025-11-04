from src.credentials.credentials_manager import *

def main():
    test_data = [
        { #test 1: too long first name
            "id": 263,
            "fName": "Aveline'); DROP TABLE Employee; --",
            "lName": "Fishbie",
            "loc": "Japan",
            "dept": "Legal",
            "title": "Manager"
        },
        { #test 2: special characters. should pass
            "id": 264,
            "fName": "Amélie",
            "lName": "Garçon-Beaumont",
            "loc": "Germany",
            "dept": "Sales",
            "title": "Sales Agent"
        },
        { #test 3: spaces in name. should pass
            "id": 265,
            "fName": "Jens",
            "lName": "van der Meer",
            "loc": "Germany",
            "dept": "Information Technology",
            "title": "Developer"
        },
        {}, #test 4: no input
        { #test 5: wrong field name
            "id": 266,
            "first_name": "Kara",
            "lName": "Lynch",
            "loc": "United States",
            "dept": "Information Technology",
            "title": "Developer"
        },
        { #test 6: missing title field
            "id": 267,
            "fName": "Noelle",
            "lName": "Stark",
            "loc": "United States",
            "dept": "Information Technology"
        },
        { #test 7: case sensitivity
            "id": 268,
            "fName": "Frederick",
            "lname": "Bumgarner",
            "loc": "United States",
            "dept": "Information Technology",
            "title": "Manager"
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