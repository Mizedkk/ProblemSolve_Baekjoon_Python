# python_crawling

## 📖 python_crawling 에 사용되는 라이브러리.

python crawling에 사용되는 라이브 러리는 다음과 같다.

```
import requests # http 요청 가져옴
from bs4 import BeautifulSoup # 이쁘게 슬라이싱함.
```

<br>

## ✏️ html 데이터를 들고와서 beautifulsoup로 정리하기

```
url = ""
html = requests.get(url) # 해당 url의 응답 상태를 가져옴 여기서 html.text 가 html 파일 본문임

soup = BeautifulSoup(html.txt, 'html.parser') # 이를 beautifulsoup 을 통해서 적정하게 html.parser을 사용해서 짤라줌
```

<br>

## ✏️ beautifulsoup 사용하기

```
tml = requests.get(url) 
soup = BeautifulSoup(html.txt, 'html.parser')

somethings = soup.find_all(class_="") # 크롬 개발자 도구를 통해서 class 찾은뒤 해당 클래스에 대한 정보를 리스트로 반환함.

for i in somethings:
    print(i.text) # 클래스로 지정된 덩어리의 text 를 반환한다.
    
    print(i.attrs['href']) # 클래스로 지정된 덩어리의 속성 중에서 href 값을 반환한다. 다른 값 mark, target 등의 값으로 대체 가능하다.

```
find_all과 select || find와 select_one 으로 구분되는데 가져오는 값이 복수 || 단수의 차이이다.

<br>

## ✏️ URL 리팩토링

url 을 보면 어떤 값을 찾고자 할 때에는 고정된 값과 변동되는 값이 있는데 이를 이용하여 처리 하는 기법이다. 

```
things = input("")
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=" + things
```
- 주의 할 점 : 사이트 마다 다르기 때문에 이를 사용하기 전에 사전적인 확인이 필요함. 

<br>

## ✏️ 요즘은..?

요즘 여러 크롤링을 해봤는데 많이 막히는 부분이 많다 다른 라이브러리를 찾아서 사용하는 법을 추천한다. 




