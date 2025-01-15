import tkinter as tk
from src.dataScraping import scrape_news

# tkinter를 활용한 뉴스 스크래핑 앱의 UI를 담당하는 클래스
class NewsApp:
    def __init__(self):
        # Tkinter 윈도우 객체 생성
        self.root = tk.Tk()
        self.root.title("뉴스 스크래핑")  # 상단(윈도우) Title

        # UI 구성 요소 추가
        tk.Label(self.root, text="키워드:").pack()  # 키워드 입력 설명 라벨
        self.keyword_entry = tk.Entry(self.root)  # 키워드 입력 필드
        self.keyword_entry.pack()

        # 스크래핑 시작 버튼 > 클릭 이벤트를 self.scrape 메서드에 연결.
        tk.Button(self.root, text="스크래핑 시작", command=self.scrape).pack()

    def scrape(self):
        # 버튼 클릭 시 실행되는 메서드
        keyword = self.keyword_entry.get()  # 입력 필드에서 키워드 가져오기
        if keyword.strip():
            scrape_news(keyword)  # 스크래핑 함수 호출
        else:
            print("키워드를 입력하세요.")  # 키워드가 없으면 메시지 출력

    def run(self):
        # Tkinter 이벤트 루프 실행
        self.root.mainloop()
