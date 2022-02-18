import json
import requests


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
def download_images(name, url):
    with open("{}.jpg".format(name), "wb") as image:
        try:
            response = requests.get(url)
        except Exception as err:
            print("Something happened {}".format(err))

        if response.status_code == 200:
            image.write(response.content)
            print("Image {} is downloaded".format(name))
        else:
            raise Exception("Something went wrong!")


download_images("new_image", "https://www.w3.org/MarkUp/Test/xhtml-print/20050519/tests/jpeg420exif.jpg")
