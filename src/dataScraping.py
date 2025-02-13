from libs.seleniumClass import SeleniumHandler
from libs.pandasClass import PandasHandler
import config

def scrape_news(keyword, filename):
    selenium = SeleniumHandler()
    selenium.open_page(config.NEWS_WEBSITE_URL)

    # 데이터 스크래핑
    data = selenium.scrape_headlines(keyword)
    selenium.close()

    # 결과 저장
    # PandasHandler.save_to_csv(data, config.OUTPUT_CSV)
    # print(f"스크래핑 완료. 결과가 {config.OUTPUT_CSV}에 저장되었습니다.")
    PandasHandler.save_to_csv(data, filename)
    print(f"스크래핑 완료. 결과가 {filename}에 저장되었습니다.")