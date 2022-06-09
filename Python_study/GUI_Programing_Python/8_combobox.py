import tkinter.ttk as ttk #combobox는 tkink.ttk에서 가져오기 때문에 임포트가 따로 필요하다.
from msilib.schema import RadioButton
from tkinter import *


root = Tk()
root.title("Nado GUI") # 창 이름설정
root.geometry("640x480") # 가로 * 세로


values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # height 는 목록의 갯수를 의미함. values는 값을 의미하고, state는 수정 불가능하게 바꿀수 있다.
readonly_combobox.current(0)
readonly_combobox.pack()



def btncmd():
    print(combobox.get()) # 선택된 값을 표시
    print(readonly_combobox.get()) # 선택된 값을 표시

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()