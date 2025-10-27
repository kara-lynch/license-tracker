from dataclasses import dataclass

FIRST_NAME_MAX_SIZE = 32
FIRST_NAME_MIN_SIZE = 2
LAST_NAME_MAX_SIZE = 32
LAST_NAME_MIN_SIZE = 2

def check_field_size(input, max_size, min_size):
    if len(input) > max_size:
        raise ValueError("too long")
    if len(input) < min_size:
        raise ValueError("too short")

@dataclass
class UserCredentials:
    id: int
    first_name: str
    last_name: str
    location: str
    department: str
    title: str

    def validate(self):
        field_name = ""
        try:
            field_name = "First name"
            check_field_size(self.first_name, FIRST_NAME_MAX_SIZE, FIRST_NAME_MIN_SIZE)
        except Exception as e:
            raise Exception(field_name + " " + e.args[0])
    
    def name(self):
        return self.first_name + " " + self.last_name
    
def main():
    test_data = [
        (
            658,
            "Joleenhjflkds;gnfklewgnrewklsw;gnwfdlk;ghweor;gwh",
            "Fishbie",
            "Japan",
            "Legal",
            "Manager"
        ),
        (
            264,
            "Amélie",
            "Garçon",
            "Germany",
            "Sales",
            "Sales Agent"
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
            print(e)
    print("List of users:")
    for user in users:
        print(user.name())

main()