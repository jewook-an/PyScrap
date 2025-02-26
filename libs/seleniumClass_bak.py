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
        time.sleep(config.SLEEP_TIME)
        # time.sleep(3)

    """
    #### 정규식 검색관련 ####
    ^       : 문자열의 시작
    $       : 문자열의 끝
    |       : OR 조건
    [가-힣] : 한글 문자 범위
    \d+     : 하나 이상의 숫자
    .*      : 모든 문자

    # 모든 헤드라인                             : all_headlines = scrape_headlines()
    # "코로나" 또는 "corona" 포함된 헤드라인    : corona_headlines = scrape_headlines("코로나|corona")
    # "2024" 로 시작하는 헤드라인               : headlines_2024 = scrape_headlines("^2024")
    # "뉴스" 로 끝나는 헤드라인                 : news_headlines = scrape_headlines("뉴스$")
    # "AI" 또는 "인공지능" 포함된 헤드라인       :
    ai_headlines = scrape_headlines("AI|인공지능")
    """
    def scrape_headlines(self, keyword=None):
        # headlines = self.driver.find_elements(By.CSS_SELECTOR, 'div.item')
        # data = [{'title': h.text, 'link': h.find_element(By.TAG_NAME, 'a').get_attribute('href')}
        # 모든 헤드라인 데이터를 우선 수집
        headlines = self.driver.find_elements(By.CSS_SELECTOR, 'a.auto-valign')
        data = [{'title': h.text, 'link': h.get_attribute('href')}
                for h in headlines]

        # AI 추가분 : keyword가 있는 경우에만 필터링 적용
        if keyword:
            try:
                """
                # 정규표현식 미적용시
                filtered_data = [
                    item for item in data
                    if keyword.lower() in item['title'].lower()
                ]
                return filtered_data
                """
                # 정규표현식 패턴 컴파일 (re.IGNORECASE : 대소문자 구분 없음)
                pattern = re.compile(keyword, re.IGNORECASE)

                # 정규표현식으로 필터링
                filtered_data = [
                    item for item in data
                    if pattern.search(item['title'])
                ]
                return filtered_data

            except re.error as e:
                # 잘못된 정규표현식 패턴이 입력된 경우 예외 처리
                print(f"정규표현식 오류: {e}")
                return []

        # keyword가 없는 경우 모든 데이터 반환
        return data

    def close(self):
        self.driver.quit()