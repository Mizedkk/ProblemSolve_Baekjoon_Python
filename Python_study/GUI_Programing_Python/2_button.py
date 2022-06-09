from tkinter import *

root = Tk()
root.title("Nado GUI") # 창 이름설정

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") # padx 좌우공간 pady 상하공간을 조절한다. 
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # width height와 padx, pady의 차이는 글자를 많이 넣었을떄, width, height는 버튼 크기가 고정이고 padx, pady는 버튼 크기가 커짐
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg는 글자색, bg는 배경색을 의미함.
btn5.pack()

photo = PhotoImage(file="image.png") # 이미지를 넣어서 버튼을 활성화 시킬수있음.
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()