import tkinter as tk
import tkinter as tk
from src.dataScraping import scrape_news
from tkinter import filedialog, ttk
import time

class NewsApp:

    #윈도우 생성
    root=tk.Tk()

    #전체 이름
    root.title('코로나 진단키트 에측도 진단 프로그램')

    #창 크기 +붙은 부분은 좌상단 떨어진 위치
    root.geometry("600x500+100+100")

    #함수들

    def make_lab14() :
        lab14.configure(text=ent12.get())

    def make_lab24() :
        lab24.configure(text=ent22.get())

    def make_lab34() :
        lab34.configure(text=ent32.get())

    def make_PPV_NPV():
        Sen=float(lab14.cget("text"))/100
        Spe=float(lab24.cget("text"))/100
        P_R=float(lab34.cget("text"))/100
        PPV=(P_R*Sen)/(P_R*Sen+(1-P_R)*(1-Spe))
        NPV=((1-P_R)*Spe)/(P_R*(1-Sen)+(1-P_R)*Spe)
        lab52.configure(text=round(PPV,3)*100)
        lab62.configure(text=round(NPV,3)*100)


    width1=8
    width2=4
    width3=8

    #1행 라벨 추가
    lab11=tk.Label(root,
        text="민감도",
        width=width1,
        height=1,
        font=('맑은 고딕',16,'bold'),
        bg='#2F5597',
        fg='white')
    lab11.grid(row=0,column=0,padx=5,pady=10)

    ent12=tk.Entry(font=('맑은 고딕',16,'bold'),bg='white',width=width3)
    ent12.grid(row=0,column=1,padx=5,pady=10)

    button13 = tk.Button(root,text='\u2192',font=('맑은 고딕',11,'bold'),bg="red",fg='white',width=width2,command=make_lab14)
    button13.grid(row=0,column=2,padx=5,pady=10)

    lab14=tk.Label(root,width=width3,height=1,font=('맑은 고딕',16,'bold'),bg='#2F5597',fg='white')
    lab14.grid(row=0,column=3,padx=5,pady=10)

    #2행 라벨 추가
    lab21=tk.Label(root,text="특이도",width=width1,height=1,font=('맑은 고딕',16,'bold'),bg='#2F5597',fg='white')
    lab21.grid(row=1,column=0,padx=5,pady=10)

    ent22=tk.Entry(font=('맑은 고딕',16,'bold'),bg='white',width=width3)
    ent22.grid(row=1,column=1,padx=5,pady=10)

    button23 = tk.Button(root,text='\u2192',font=('맑은 고딕',11,'bold'),bg="red",fg='white',width=width2,command=make_lab24)
    button23.grid(row=1,column=2,padx=5,pady=10)

    lab24=tk.Label(root,width=width3,height=1,font=('맑은 고딕',16,'bold'),bg='#2F5597',fg='white')
    lab24.grid(row=1,column=3,padx=5,pady=10)

    #3행 라벨 추가
    lab31=tk.Label(root,text="발생률",width=width1,height=1,font=('맑은 고딕',16,'bold'),bg='#2F5597',fg='white')
    lab31.grid(row=2,column=0,padx=5,pady=10)

    ent32=tk.Entry(font=('맑은 고딕',16,'bold'),bg='white',width=width3)
    ent32.grid(row=2,column=1,padx=5,pady=10)

    button33 = tk.Button(root,text='\u2192',font=('맑은 고딕',11,'bold'),bg="red",fg='white',width=width2,command=make_lab34)
    button33.grid(row=2,column=2,padx=5,pady=10)

    lab34=tk.Label(root,width=width3,height=1,font=('맑은 고딕',16,'bold'),bg='#2F5597',fg='white')
    lab34.grid(row=2,column=3,padx=5,pady=10)

    #4행 라벨 추가
    button41 = tk.Button(root,text='결과 계산하기(클릭)',font=('맑은 고딕',16,'bold'),bg="red",fg='white',command=make_PPV_NPV)
    button41.grid(row=3,column=0,padx=5,pady=10,columnspan=4,sticky='we')

    #5행 라벨 추가
    lab51=tk.Label(root,text="양성예측도 (양성인데 진짜걸림)",height=1,font=('맑은 고딕',16,'bold'),bg='#2F5597',fg='white')
    lab51.grid(row=4,column=0,padx=5,pady=10,columnspan=3,sticky='we')

    lab52=tk.Label(root,width=width3,height=1,font=('맑은 고딕',16,'bold'),bg='yellow',fg='black')
    lab52.grid(row=4,column=3,padx=5,pady=10)

    #6행 라벨 추가
    lab61=tk.Label(root,text="음성예측도 (음성인데 진짜 안걸림)",height=1,font=('맑은 고딕',16,'bold'),bg='#2F5597',fg='white')
    lab61.grid(row=5,column=0,padx=5,pady=10,columnspan=3,sticky='we')

    lab62=tk.Label(root,width=width3,height=1,font=('맑은 고딕',16,'bold'),bg='yellow',fg='black')
    lab62.grid(row=5,column=3,padx=5,pady=10)