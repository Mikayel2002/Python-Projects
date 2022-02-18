import json


def login_check(func: callable) -> callable:
    def decorated(*args, **kwargs):
        username = input("Username: ")
        password = input("Password: ")

        result = func(*args, **kwargs)

        with open("user_information.json") as file:
            data = json.load(file)

        for i in data["user"]:
            if username == i["username"] and password == i["password"]:
                return result
            else:
                raise Exception("Authentication Failed")

    return decorated


@login_check
def hello(name):
    return "Hello {}".format(name)


print(hello("Mikayel"))
