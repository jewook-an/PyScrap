from libs.seleniumClass import SeleniumHandler
from libs.pandasClass import PandasHandler
import config

def scrape_news(media, keyword, filename):
    selenium = SeleniumHandler()
    selenium.open_page(config.MEDIA_SOURCES[media])

    # 데이터 스크래핑
    data = selenium.scrape_headlines(media, keyword)
    selenium.close()

    # 결과 저장
    PandasHandler.save_to_csv(data, filename)
    print(f"스크래핑 완료. 결과가 {filename}에 저장되었습니다.")