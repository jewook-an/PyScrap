## 20250107 작업 >> keyword, filename 저장까지 >> 차후 filepath 추가해 작업 필요


import tkinter as tk
from src.dataScraping import scrape_news
from tkinter import filedialog, ttk
import time

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

        # 파일 이름 입력 필드
        tk.Label(self.root, text="저장 파일 이름 (확장자 제외):").pack()
        self.filename_entry = tk.Entry(self.root)
        self.filename_entry.pack()

        # 진행 상태 표시
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack()

        # 결과 표시 영역
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack()

        # 저장 경로 선택 버튼
        tk.Button(self.root, text="파일 저장 경로 선택", command=self.select_path).pack()
        self.path_label = tk.Label(self.root, text="경로가 선택되지 않음")
        self.path_label.pack()

        # 스크래핑 시작 버튼 > 클릭 이벤트를 self.scrape 메서드에 연결.P
        tk.Button(self.root, text="스크래핑 시작", command=self.scrape).pack()

        self.file_path = None  # 선택된 파일 경로

    def select_path(self):
        # self.file_path = filedialog.asksaveasfilename(defaultextension=".csv",
        #                                               filetypes=[("CSV files", "*.csv")])
        self.file_path = filedialog.askdirectory()
        if self.file_path:
            self.path_label.config(text=f"저장 경로: {self.file_path}")

    def scrape(self):
        # self.result_text.delete("1.0", tk.END)      # 1.0 첫번째 줄, 첫번째 글자 부터 end 마지막 까지 지우기
        # 입력값 가져오기
        keyword = self.keyword_entry.get().strip()  # 키워드 입력값 (입력 필드)
        filename = self.filename_entry.get().strip()  # 파일 이름 입력값

        # 입력값 검증
        if not keyword:
            # print("키워드를 입력하세요.")
            self.result_text.insert(tk.END, "키워드를 입력하세요.\n")
            return
        if not filename:
            # print("저장 파일 이름을 입력하세요.")
            self.result_text.insert(tk.END, "저장 파일 이름을 입력하세요.\n")
            return

        # 스크래핑 함수 호출 (데모를 위해 출력)
        print(f"키워드: {keyword}")
        print(f"저장 파일 이름: {filename}.csv")

        # 실제 스크래핑 함수 호출
        # scrape_news(keyword, f"{filename}.csv")

        self.result_text.delete("1.0", tk.END)

        if self.file_path:
            # 스크래핑 함수 호출 및 결과 저장
            print(f"'{keyword}' 키워드로 데이터를 {self.file_path}에 저장합니다.")
            scrape_news(keyword, f"{filename}.csv")

            self.result_text.insert(tk.END, f"'{keyword}' 키워드로 스크래핑 시작...\n")
            self.result_text.insert(tk.END, "스크래핑 완료!\n")

        else:
            # print("파일 저장 경로를 선택하세요.")
            self.result_text.insert(tk.END, "파일 저장 경로를 선택하세요.\n")

    def run(self):
        # Tkinter 이벤트 루프 실행
        self.root.mainloop()
