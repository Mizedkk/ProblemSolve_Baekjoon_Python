from tkinter import *

root = Tk()
root.title("Nado GUI") # 창 이름설정



#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, text="파일추가", padx=5, pady=5, width=12)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택삭제", padx=5, pady=5, width=12)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack()

Scrollbar


root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가(창 크기 변경 불가)
root.mainloop()