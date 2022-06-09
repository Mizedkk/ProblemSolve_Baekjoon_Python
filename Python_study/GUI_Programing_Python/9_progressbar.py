import time
import tkinter.ttk as ttk #progressbar는 tkink.ttk에서 가져오기 때문에 임포트가 따로 필요하다.
from msilib.schema import RadioButton
from tkinter import *


root = Tk()
root.title("Nado GUI") # 창 이름설정
root.geometry("640x480") # 가로 * 세로


# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #indeterminate 결정되지 않은
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") #indeterminate 결정되지 않은
# progressbar.start(10) # 10 ms 마다 움직임. 
# progressbar.pack()


# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01) # 0.01 초 대기
        
        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())


btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()