import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko"
}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a)
print(soup.a.attrs)
print(soup.a['href'])
print(soup.find("a", attrs={"class": "Nbtn_upload"}))
print(soup.find(attrs={"class": "Nbtn_upload"}))
print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())
print(rank1.next_sibling.next_sibling)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

print(rank1.parent)
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="99강화나무몽둥이-17화. ONE LOVE (1)")
print(webtoon)

cartoons = soup.find_all("a", attrs={"class": "title"})
for cartoon in cartoons:
    print(cartoon.get_text())
