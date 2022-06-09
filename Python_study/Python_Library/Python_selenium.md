# pyauto selenium

## 📖 selenium 라이브러리
셀레니움은 driver 등을 이용하여 동적으로 웹을 컨트롤 할수 있게 만들어주는 라이브러리다.
준비 내용은 다음과 같다.

```
from selenium import webdriver # 셀레니움이 깔려있어야함.

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() # 각 크롬에 맞는 드라이버가 깔려있어야함

driver.get("http://www.google.com") # 열고 싶은 사이트
```

<br>

## ✏️ 셀레니움 페이지 열고 요소에 찾아가서 값 넣기
```
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.google.com")

elem = driver.find_element_by_name("") # name 요소가 q인 것을 찾기(구글 검색창)


elem.send_keys("아이유") # elem 값에 "아이유"라는 값을 보내기
elem.send_keys(Keys.RETURN) # 엔터 입력

```

## ✏️ 이미지 저장하기 

```
import urllib.request

driver.find_element_by_css_selector("").click() # css가 "" 인것을 찾고 그것을 클릭 하기

driver.find_element_by_css_selector("").send_keys("") # css가 "" 인것을 찾고 거기에 ""값을 넣기

imgUrl = driver.find_element_by_css_selector("").get_attribute("src") # css가 "" 인것에서 속성 src 값을 반환하기

urllib.request.urlretrieve(imgUrl, "test.jpg") # 해당 이미지 주소를 test.jpg 파일로 변환
```

만약 여러 이미지가 있다면 elements로 바꿔서 리스트에 담고 for 문을 돌려가면서 하나씩 저장하는 것을 하면 된다. 