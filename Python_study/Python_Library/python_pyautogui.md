# pyauto gui

## 📖 pyautogui 라이브러리
마우스와 키보드 를 자동으로 움직일 수 있도록 하는 라이브러리
다음 라이브러리를 사용하기 위해서는 밑에 있는 것들을 다운 받아야 원활히 사용이 가능하다.

```
pip install pyautogui # 해당 라이브러리쓰는데 사용

pip install opencv-python # 이미지 처리에 사용

pip install pillow # 이미지 처리에 사용
```

<br>

## ✏️ 시간 컨트롤
```
import time

time.sleep(t) # 상수 t 만큼 기다린다.
```

<br>

## ✏️ 마우스 컨트롤
```
pyautogui.position() # 마우스 위치값 반환

pyautogui.moveTo(x, y, t) # 마우스를 x, y 좌표로 t 시간 만큼 이동 t 없을 시 바로 이동

pyautogui.moveRel(x, y, t) # 현재 마우스 시점에서 x, y 만큼 t 시간 만큼 이동 t 없을시 바로 이동

pyautogui.click(clicks=2, interval=2) # 마우스를 클릭함. 옵션으로는 2번 클릭하고, 2초뒤에 다시 클릭함.

pyautogui.doubleClick() # 마우스 더블클릭

pyautogui.mouseInfo() # 마우스 해당위치와, RGB 색상 실시간을 얻을 수 있는 창이 열린다.
```

<br>

## ✏️ 키보드 컨트롤
```
pyautogui.write(string) # 키보드로 string을 입력한다. 

pyautogui.write(['a', 'b', 'c', 'enter'], interval=0.2) # 키보드 a, b, c, 엔터를 순서대로 입력한다. interval 은 중간 간격마다 텀을 준다는 의미

pyautogui.press('원하는 키') # 원하는키를 누른다.

pyautogui.hotkey("ctrl", "c") # 조합 키 입력을 한다.
```

- 주의 할 점 : 만약 .txt 파일을 더블클릭해서 열려고 할 경우에 열면서 바로 pyautogui.write. ~ 을 하게 되면 글씨 입력이 제대로 안되기 때문에 time.sleep(1) 를 이용하여야 제대로 작동한다.

<br>

## ✏️ 이미지 컨트롤

```
import pyautogui

pyautogui.screenshot('1.png', region=(1539, 705, 50, 50)) # 해당 x, y 좌표에서 50, 50 크기의 사진을 저장

i = pyautogui.locateCenterOnScreen('사진경로', confidence=0.7) # 사진 경로와 맞는 것을 찾아서 그 좌표를 i 에 저장, confidence 옵션은 정확도 70이상을 의미

pyautogui.click(i) # 사진에 맞는 것을 찾아 클릭함.
```

- 주의 할 점 : 내 눈에 보이는 정도의 속도로 하는거라서 진짜 완전 빠른 속도로는 불가능하고 살짝 불안정하기도 함

<br>

## ✏️ 알람 컨트롤

```
import pyautogui as pg

alert = pyautogui.alert(text, title, button_string , timeout) # timeout에 3000 넣으면 3초 진행
print(alert)

pg.confrim(string, title, (button1_string, button2_string), titmeout) # string 내용에 대한 확인창을 뜨게 만듬

pg.prompt(string, title, default, titmeout) # 텍스트 입력 받는 추가 창을 뛰움, default는 창이 뜰때 기본 값을 의미

pg.password(string, title, default, mask, titmeout) # 패스워드 입력 하는 창을 뛰움, mask를 통해 기본값인 * 을 다른 것으로 변경 가능
```

