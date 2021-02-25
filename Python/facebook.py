from bs4 import BeautifulSoup as BS4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import re
webdriverLocation = 'Python\\Chrome_88.0.4324.96\\chromedriver.exe'

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
options.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications" : 2})
driver = webdriver.Chrome(webdriverLocation, chrome_options = options)

email = ''
password = ''

# 로그인
driver.get('https://www.facebook.com')
driver.find_element_by_xpath('//*[@id="email"]').click()
driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
driver.implicitly_wait(3)


# 게시글 불러오기를 위한 5초간 스크롤 다운 실행
start = datetime.datetime.now()
end = start + datetime.timedelta(seconds=5)
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
    if datetime.datetime.now() > end:
        break
html = driver.page_source
soup = BS4(html,'html.parser')
content_list = soup.find_all(attrs={'data-pagelet': re.compile('^FeedUnit')})

# 페이지 사진
# <g mask="url(#jsc_c_3p)">
# 페이지 제목
# <strong><span>서머너즈 워: 백년전쟁</span></strong>

# 본문
# <div dir="auto" style="text-align: start;">
# 이미지
# <img alt="" class=
input('')