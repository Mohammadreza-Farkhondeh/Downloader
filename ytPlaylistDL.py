from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

URL = input('playlist page URL: ')
driver = webdriver.Chrome()
driver.get(URL)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_links = soup.find_all('a', {'class': "yt-simple-endpoint style-scope ytd-playlist-video-renderer"})

Quality = input('Quality (1080, 720, 480, 360, 240, 144): ')


def find_quality(s):
    trs = s.find_all('tr')
    for tr in trs:
        td = tr.find(td)
        if td.text == f'(.mp4) {Quality}p':
            return tr


def wait_to_convert_then_return_href(tr):
    td = tr.find_all('td')[2]
    btn = td.find('button')
    a = btn.find('a')
    if a.text != "Download":
        time.wait(1)
        wait_to_convert_then_return_href(s)
    else:
        href = a['href']
        return href


def click_to_convert(tr):
    td = tr.find_all('td')[2]
    btn = td.find('button')
    span = btn.find('span')
    if span.text == "Convert":
        btn.click()


for i in range(len(all_links)):
    all_links[i] = 'https://www.youtubepi.com'+all_links[i]['href']

print(all_links)

for i in range(len(all_links)):
    driver.switch_to.window(driver.window_handles[0])
    driver.get(all_links[i])
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tr = find_quality(s)
    click_to_convert(tr)
    href = wait_to_convert_then_return_href(tr)
    driver.send_keys(Keys.CONTROL + 't')
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(href)

