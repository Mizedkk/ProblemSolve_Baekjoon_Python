#  pyinstaller

## 📖 pyinstaller 라이브러리
코딩한 파이썬 프로그램을 파이썬에 대해 전혀 모르는 사람도 사용 할 수 있도록 실행 파일로 만들어주는 파이썬 패키지이다.

```
pip install pyinstaller
```

<br>

## ✏️ 사용 할 만한 기능
```
# pyinstaller 는 터미널에서 실행하여아 한다.

pyinstaller  -icon -f -w 파이썬 파일명.py # -f, -w 는 옵션이며 아래와 같다.

1) -icon, '--icon = ico 파일의 경로'
 '--icon = ico 파일의 경로' 로 exe 파일 이미지를 바꿔준다.


2) -F, --onefile
방금 전과 같이 지저분하게 파일이 생성되지 않고, 실행파일 1개만 생성되도록 해주는 설정입니다.

3) -w, --windowed, --noconsole
기본적으로 실행 파일을 실행하면 표준 I/O용 콘솔 창(까만 창)을 열도록 되어있는데 이걸 뜨지 않도록 하는 옵션입니다.
```