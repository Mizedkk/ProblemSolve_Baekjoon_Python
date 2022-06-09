#  zipfile

## 📖 zipfile 라이브러리
zipfile 모듈은 압출된 폴더를 다운 받거나 압축해서 업로드 할때 사용되는 표준 라이브러리이다.


<br>

## ✏️ 사용 할 만한 기능
```
import zipfile
import os

file_list = ["파일들 리스트"] # os.listdir 이용하는 것이 편리

# 파일 압축

with zipfile.ZipFile("name.zip", "w") as zip: #zip 으로 open 
    for i in file_list: 
        zip.write(i) # 파일 압축해서 넣음
    
    # zip.close() # 집을 닫음 with 없이 했다면 꼭 써줘야함


# 압축 해제

ZipFile.extractall(path=None, members=None, pwd=None) # path는 경로, members는 압축된 파일중에서 선택적으로 파일 압축헤제, pwd는 패스워드 걸린 파일에 사용되는 암호


```