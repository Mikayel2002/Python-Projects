import requests
import threading
import json


with open("images.json") as json_file:
    data = json.load(json_file)


def download_images(name, url):
    with open("{}.jpg".format(name), "wb") as image:
        try:
            response = requests.get(url)
        except Exception as err:
            print("Something happened {}".format(err))

        if response.status_code == 200:
            image.write(response.content)
            print("Image {} is downloaded".format(name))


thread_list = []

for item in data:
    t = threading.Thread(target=download_images, args=(item["name"], item["url"]))
    thread_list.append(t)

for thread in thread_list:
    thread.start()
