import requests


class A:
    def __init__(self, response_1, response_2):
        self.response_1 = response_1
        self.response_2 = response_2

    def download_jpeg_image(self):
        self.response_1 = requests.get('https://upload.wikimedia.org/wikipedia/commons/2/23/Lake_mapourika_NZ.jpeg')

        with open("new_image_1.jpeg", "wb") as file_1:
            file_1.write(self.response_1.content)

    def download_png_image(self):
        self.response_2 = requests.get('https://imgs.xkcd.com/comics/python.png')

        with open("new_image_2.png", "wb") as file_2:
            file_2.write(self.response_2.content)


a = A('https://upload.wikimedia.org/wikipedia/commons/2/23/Lake_mapourika_NZ.jpeg', 'https://imgs.xkcd.com/comics/python.png')
a.download_jpeg_image()
a.download_png_image()
