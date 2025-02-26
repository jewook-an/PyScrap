from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import config
import re       # 정규 표현식 관련련

class SeleniumHandler:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_page(self, url):
        self.driver.get(url)
        # time.sleep(3)
        time.sleep(config.SLEEP_TIME)

    def scrape_headlines(self, keyword=None):
        # 모든 헤드라인 데이터를 우선 수집
        headlines = self.driver.find_elements(By.CSS_SELECTOR, 'a.auto-valign')
        data = [{'title': h.text, 'link': h.get_attribute('href')}
                for h in headlines]

        # keyword 있을때 필터링
        if keyword:
            try:
                # 정규표현식 패턴 컴파일 (re.IGNORECASE : 대소문자 구분 없음)
                pattern = re.compile(keyword, re.IGNORECASE)

                # 정규표현식으로 필터링
                filtered_data = [
                    item for item in data
                    if pattern.search(item['title'])
                ]
                return filtered_data

            # 잘못된 정규표현식 패턴 입력시 예외 처리
            except re.error as e:
                print(f"정규표현식 오류: {e}")
                return []

        # keyword 없을때 모든 데이터 반환
        return data

    def close(self):
        self.driver.quit()