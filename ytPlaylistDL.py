from selenium import webdriver
from bs4 import BeautifulSoup
import time

URL = input('playlist page URL: ')
urlToDL = URL.split('.com')
urlToDL = urlToDL[0]+'pp.com'+urlToDL[1]
driver = webdriver.Firefox()
driver.get(URL)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_links = soup.find_all('a', {'class': "yt-simple-endpoint style-scope ytd-playlist-video-renderer"})

Quality = input('Quality (1080, 720, 480, 360, 240, 144): ')


def wait_to_convert_then_return_href(s):
    div = s.find('div', {'id': "process-result"})
    if div.text == "":
        time.wait(1)
        wait_to_convert_then_return_href(s)
    elif div.text == " Download .mp4":
        href = div.find('a')['href']
        return href


for i in range(len(all_links)):
    all_links[i] = urlToDL+all_links[i]['href']
    driver.get(all_links[i])
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    buttons = soup.find_all('button', {'class': 'btn btn-success'})

    for btn in buttons:
        if btn.text == Quality:
            btn.click()

    href = wait_to_convert_then_return_href(soup)
    webdriver.Firefox().get(href)

