import requests


class Quotes(object):
    def __init__(self, url):
        self.url = url

    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()

    def txt_create(self):
        if self.response.status_code == 200:
            for i in self.data:
                for j in i.values():
                    with open("quotes.txt", "w") as txt:
                        txt.write(j)
        else:
            raise Exception("Something went wrong!")


x = Quotes("https://zenquotes.io/api/random")
print(x.txt_create())
