import tkinter as tk
from src.dataScraping import scrape_news
from tkinter import filedialog, ttk
import time
import config

class NewsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("뉴스 스크래핑")
        self.root.geometry("800x600+100+100")

        # UI 구성 요소 추가 (padx:x축 padding / pady: y축 padding / sticky: 위치)
        # UI 참고 : https://information-factory.tistory.com/289
        l0 = tk.Label(self.root, text="언론사:", font=('맑은 고딕', 12, 'bold'))
        self.media_var = tk.StringVar()
        media_options = list(config.MEDIA_SOURCES.keys())
        media_select = ttk.Combobox(self.root, textvariable=self.media_var, values=media_options, font=('맑은 고딕', 12, 'bold'))

        l0.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        media_select.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky='ew')

        l1 = tk.Label(self.root, text="키워드:", font=('맑은 고딕', 12, 'bold'))
        k1 = self.keyword_entry = tk.Entry(self.root, font=('맑은 고딕', 12, 'bold'))

        l1.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        k1.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky='ew')

        l2 = tk.Label(self.root, text="저장 파일명 (확장자 제외):", font=('맑은 고딕', 12, 'bold'))
        k2 = self.filename_entry = tk.Entry(self.root, font=('맑은 고딕', 12, 'bold'))

        l2.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        k2.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky='ew')

        pg = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        pg.grid(row=3, column=0, columnspan=3, padx=10, pady=2, sticky='ew')

        self.rtext = tk.Text(self.root, height=10, width=50, font=('맑은 고딕', 12, 'bold'))
        self.rtext.grid(row=4, column=0, columnspan=3, padx=10, pady=2, sticky='ew')

        btn1 = tk.Button(self.root, text="파일 저장 경로 선택", command=self.select_path, font=('맑은 고딕', 12, 'bold'))
        self.plabel = tk.Label(self.root, text="경로가 선택되지 않음", font=('맑은 고딕', 12, 'bold'))

        btn1.grid(row=5, column=0, padx=10, pady=5, sticky='ew')
        self.plabel.grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky='ew')

        btn2 = tk.Button(self.root, text="스크래핑 시작", command=self.scrape, font=('맑은 고딕', 12, 'bold'))
        btn2.grid(row=6, column=0, columnspan=3, padx=10, pady=5, sticky='ew')

        self.file_path = None

    def select_path(self):
        self.file_path = filedialog.askdirectory()
        if self.file_path:
            self.plabel.config(text=f"저장 경로: {self.file_path}")

    def scrape(self):
        media = self.media_var.get().strip()
        keyword = self.keyword_entry.get().strip()
        filename = self.filename_entry.get().strip()
        keywordsavetext = ""

        if not media:
            self.rtext.insert(tk.END, "언론사를 선택하세요.\n")
            return

        if not keyword:
            self.rtext.insert(tk.END, "키워드 없이 스크래핑을 시작 합니다.\n")
            keywordtext = f"키워드 없이 스크래핑 시작..."
            keywordsavetext = f"키워드 없이 데이터를 {self.file_path}에 저장합니다."
        else:
            self.rtext.insert(tk.END, "입력된 키워드로 스크래핑을 시작 합니다.\n")
            keywordtext = f"'{keyword}' 키워드로 스크래핑 시작..."
            keywordsavetext = f"'{keyword}' 키워드로 데이터를 {self.file_path}에 저장합니다."

        if not filename:
            self.rtext.insert(tk.END, "저장 파일 이름을 입력하세요.\n")
            return

        self.rtext.delete("1.0", tk.END)

        if self.file_path:
            print(f"{keywordsavetext}")
            totFilePath = self.file_path + f"/{filename}.csv"
            scrape_news(media, keyword, f"{totFilePath}")

            self.rtext.insert(tk.END, f"{keywordtext}\n")
            self.rtext.insert(tk.END, "스크래핑 완료!\n")
        else:
            self.rtext.insert(tk.END, "파일 저장 경로를 선택하세요.\n")

    def run(self):
        self.root.mainloop()
