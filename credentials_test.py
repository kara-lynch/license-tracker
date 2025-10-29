from src.credentials.credentials_manager import *

def main():
    test_data = [
        (
            263,
            "Ava'); DROP TABLE Employee; --",
            "Fishbie",
            "Japan",
            "Legal",
            "Manager"
        ),
        (
            264,
            "Amélie",
            "Garçon-Beaumont",
            "Germany",
            "Sales",
            "Sales Agent"
        ),
        (
            265,
            "Jens",
            "van der Meer",
            "Germany",
            "Information Technology",
            "Developer"
        )
    ]
    users = []
    for test in test_data:
        new_user = UserCredentials(test[0], test[1], test[2], test[3], test[4], test[5])
        try:
            new_user.validate()
            users.append(new_user)
            print(f"{new_user.name()} added successfully")
        except Exception as e:
            print(f"Cannot add {new_user.name()}: {e.args[0]}")
    print("List of users:")
    for user in users:
        print(user.name())

main()