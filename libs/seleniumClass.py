from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import config
# 정규 표현식 관련
import re

class SeleniumHandler:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_page(self, url):
        self.driver.get(url)
        # time.sleep(3)
        time.sleep(config.SLEEP_TIME)

    def scrape_headlines(self, media, keyword=None):
        # 모든 헤드라인 데이터를 우선 수집 : 언론사에 따라 다른 CSS 셀렉터 사용
        if media == "SPOTV":
            headlines = self.driver.find_elements(By.CSS_SELECTOR, 'a.auto-valign')
            data = [{'title': h.text, 'link': h.get_attribute('href')} for h in headlines]
        elif media == "NaverSports":
            headlines = self.driver.find_elements(By.CSS_SELECTOR, 'a.link_today')
            data = [{'title': h.get_attribute('title'), 'link': h.get_attribute('href')} for h in headlines]
        elif media == "언론사3":
            headlines = self.driver.find_elements(By.CSS_SELECTOR, 'a.headline')
            data = []
        else:
            headlines = []
            data = []

        # keyword 있을때 필터링
        if keyword:
            try:
                # 정규표현식 패턴 컴파일 (re.IGNORECASE : 대소문자 구분 없음)
                pattern = re.compile(keyword, re.IGNORECASE)
                # 정규표현식으로 필터링
                filtered_data = [item for item in data if pattern.search(item['title'])]

                return filtered_data
            except re.error as e:
                print(f"정규표현식 오류: {e}")
                return []

        # keyword 없을때 모든 데이터 반환
        return data

    def close(self):
        self.driver.quit()