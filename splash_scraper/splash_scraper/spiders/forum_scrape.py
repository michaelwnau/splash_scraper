import requests
from bs4 import BeautifulSoup

url = "https://www.diychatroom.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

for thread in soup.find_all("div", class_="structItem-title"):
    print(thread.text.strip())
