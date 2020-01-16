import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
import re





class googleSearch:

    def __init__(self,searUser):
        self.searUser = searUser
        self.listResult = list()

    def update(self):
        search_result_list = list(search(self.searUser, tld="co.in",lang="ru", num=10, stop=3, pause=2.5))
        page = requests.get(search_result_list[0])
        soup =  BeautifulSoup(page.content, "html.parser")

        for tag in soup.find_all("p"):
            self.listResult.append(tag.text)

        return "".join(self.listResult)
