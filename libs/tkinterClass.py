import tkinter as tk
from src.dataScraping import scrape_news
from tkinter import filedialog, ttk
import time

class NewsApp:
    def __init__(self):

        self.root = tk.Tk()                        # Tkinter 윈도우 객체 생성
        self.root.title("뉴스 스크래핑")            # 상단(윈도우) Title
        self.root.geometry("800x600+100+100")      # geometry("가로x세로+x좌표+y좌표")

        # UI 구성 요소 추가 : .pack() > 창에 표시하는 역할 > grid 와 pack 는 함께 쓰지 못함
        l1 = tk.Label(self.root, text="키워드:")  # 키워드 입력 설명 라벨
        k1 = self.keyword_entry = tk.Entry(self.root)  # 키워드 입력 필드

        l1.grid(row=0, column=0)
        k1.grid(row=0, column=1, columnspan=2, sticky='ew')

        # 파일 이름 입력 필드
        l2 = tk.Label(self.root, text="저장 파일 이름\n(확장자 제외):")
        k2 = self.filename_entry = tk.Entry(self.root)

        l2.grid(row=1, column=0)
        k2.grid(row=1, column=1, columnspan=2, sticky='ew')

        # 진행 상태 표시
        pg = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        pg.grid(row=2, column=0, columnspan=3, sticky='ew')

        # 결과 표시 영역
        self.rtext = tk.Text(self.root, height=10, width=50)
        self.rtext.grid(row=3, column=0, columnspan=3, sticky='ew')

        # 저장 경로 선택 버튼
        btn1 = tk.Button(self.root, text="파일 저장 경로 선택", command=self.select_path)
        self.plabel = tk.Label(self.root, text="경로가 선택되지 않음")

        btn1.grid(row=4, column=0, sticky='ew')
        self.plabel.grid(row=4, column=1, columnspan=2, sticky='ew')

        # 스크래핑 시작 버튼 > 클릭 이벤트를 self.scrape 메서드에 연결
        btn2 = tk.Button(self.root, text="스크래핑 시작", command=self.scrape)
        btn2.grid(row=5, column=0, columnspan=3, sticky='ew')

        self.file_path = None  # 선택된 파일 경로

    def select_path(self):
        self.file_path = filedialog.askdirectory()
        if self.file_path:
            self.plabel.config(text=f"저장 경로: {self.file_path}")

    def scrape(self):
        # self.result_text.delete("1.0", tk.END)      # 1.0 첫번째 줄, 첫번째 글자 부터 end 마지막 까지 지우기
        # 입력값 가져오기
        keyword = self.keyword_entry.get().strip()  # 키워드 입력값 (입력 필드)
        filename = self.filename_entry.get().strip()  # 파일 이름 입력값
        keywordsavetext = ""

        # 입력값 검증
        if not keyword:
            self.rtext.insert(tk.END, "키워드 없이 스크래핑을 시작 합니다.\n")

            keywordtext = f"키워드 없이 스크래핑 시작..."
            keywordsavetext = f"키워드 없이 데이터를 {self.file_path}에 저장합니다."
            # return
        else:
            self.rtext.insert(tk.END, "입력된 키워드로 스크래핑을 시작 합니다.\n")

            keywordtext = f"'{keyword}' 키워드로 스크래핑 시작..."
            keywordsavetext = f"'{keyword}' 키워드로 데이터를 {self.file_path}에 저장합니다."

        if not filename:
            self.rtext.insert(tk.END, "저장 파일 이름을 입력하세요.\n")
            return

        # print(f"키워드: {keyword}")
        # print(f"저장 파일 이름: {filename}.csv")

        self.rtext.delete("1.0", tk.END)

        if self.file_path:
            # 스크래핑 함수 호출 및 결과 저장
            print(f"{keywordsavetext}")
            totFilePath = self.file_path + f"/{filename}.csv"
            scrape_news(keyword, f"{totFilePath}")

            self.rtext.insert(tk.END, f"{keywordtext}\n")
            self.rtext.insert(tk.END, "스크래핑 완료!\n")

        else:
            self.rtext.insert(tk.END, "파일 저장 경로를 선택하세요.\n")

    def run(self):
        # Tkinter 이벤트 루프 실행
        self.root.mainloop()
