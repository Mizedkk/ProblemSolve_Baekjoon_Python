#  pyperclip

## 📖 pyperclip 라이브러리
클립보드 라이브러리 이다. 외부 라이브러리 이기 때문에 설치를 해줘야 한다. 

```
pip install pyperclip
```

<br>

## ✏️ 사용 할 만한 기능
```
import pyperclip
import pyautogui as pg


pyperclip.copy("string") # string을 클립보드에 저장한다.
pg.hotkey("ctrl", "v") # 클립보드 내용을 붙여 넣는다.
```