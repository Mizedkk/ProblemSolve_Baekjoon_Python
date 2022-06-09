#  schedule

## 📖 schedule 라이브러리
schedule 은 시간에 맞춰 어떤 일을 할 때 사용하는 패키지 이다. 

```
pip install schedule
```

<br>

## ✏️ 사용 할 만한 기능
```
import schedule
import time

schedule.every(s).seconds.do(함수) # s 초 마다 한번씩 함수 실행

schedule.every(s).minutes.do(함수) # s 분 마다 한번씩 함수 실행

schedule.every(s).hour.do(함수) # s 시간 마다 한번씩 함수 실행

schedule.every(s).days.do(함수) # s 일 마다 한번씩 함수 실행

schedule.every(s).weeks.do(함수) # s 주마다 한번씩 함수 실행

schedule.every().day.at("13:30").do(함수) # 매일 정해진 시간에 따라 실행

# 만약에 인자를 받는 함수가 존재한다면 다음과 같이 사용

def message2(text):
    print(text)

schedule.every(2).seconds.do(message2,'2초마다 알려줄게요')
```

## ✏️ 사용 방법

```
# step1.관련 패키지 및 모듈 import
import schedule
import time

# step2.실행할 함수 선언


def message():
    print("스케쥴 실행중...")


# step3.실행 주기 설정
schedule.every(1).seconds.do(message)

# step4.스캐쥴 시작
while True:
    schedule.run_pending() # 스케쥴 실행
    time.sleep(1)
```

## ✏️ 중지 방법

```
1. while문에 조건을 걸어서 무한루프를 종료시키고 파이썬 파일을 종료한다.

2. sys 모듈의 exit( ) 함수로 파이썬 파일을 강제 종료

3. schedule 패키지의 cancel_job( ) 함수 사용
```