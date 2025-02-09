#  re

## 📖 re 라이브러리
정규 표현식 모듈이다. 어떤 문장을 찾거나 패턴을 찾을 때 많이 사용되는 것이다. 

```
import re
```

<br>

## ✏️ 정규 표현식의 기초, 메타 문자
```
. ^ & * + ? { } [ ] \ | ( ) 가 존재한다.


# 문자 클래스 []
[abc] 의미 : a,b,c 중 한개의 문자와 매치
문자 사이에 - (하이폰) 을 사용하면 from - to 를 의미
[a-c] == [abc] : 같은 의미
[a-zA-Z] : 알파벳모두
[0-9] : 숫자모두


# - (하이폰)
from - to 의 의미를 가짐

# ^ 
부정의 의미를 가짐 
[^0-9] : 숫자가 아닌 문자 매치

# 자주 사용하는 문자 클래스
\d : 숫자와 매치 [0-9] 와 동일
\D : 숫자가 아닌 것과 매치 [^0-9] 와 동일
\s : whitespace 문자와 매치.
\S : whitespace 가 아닌 것과 매치
\w : 문자 + 숫자와의 매치
\W : 문자 + 숫자가 아닌 문자와 매치

# Dot(.)
줄바꿈 문자인 \n 을 제외한 모든 문자와 매치
a.b => aab, a0b 와 매치, 단 abc 는 a와 b 사이 아무것도 없어서 매치 안됨!

# 반복(*)
반복의 의미를 가짐
ca*t => ct, cat, caat , caaaaat 와 매칭

# 반복(+)
반복의 의미를 가짐
ca+t => cat, caat , caaaaat 와 매칭 단 a는 무조건 하나 이상 존재 하여야 한다.

# 반복 제어({m, n}, ?)
ca{2}t => caat
ca{2, 5}t => caat, caaat, caaaat, caaaaat

# 있거나 없거나 ?
있거나 없을수도 있는 메타문자를 의미
ab?c => abc, ac
```


<br>

## ✏️ re 모듈 사용하기
```
import re
p = re.compile('[a-z]+')

match() : 문자열의 처음부터 정규식과 매치되는지 조사한다.

search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.

findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.

finditer() :정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.

- match 객체의 메서드
group()	매치된 문자열을 돌려준다.

start()	매치된 문자열의 시작 위치를 돌려준다.

end()	매치된 문자열의 끝 위치를 돌려준다.

span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
```

## ✏️ 메타문자 

```
# | 
| 메타 문자는 or 과 동일한 의미로 사용된다. 


# ^
^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다. 

# $
$ 메타 문자는 문자열의 끝과 매치함을 의미한다.

# \A
\A는 문자열의 처음과 매치됨을 의미한다. ^ 메타 문자와 동일한 의미이지만 re.MULTILINE 옵션을 사용할 경우에는 다르게 해석된다.

# \Z
\Z는 문자열의 끝과 매치됨을 의미한다. 이것 역시 \A와 동일하게 re.MULTILINE 옵션을 사용할 경우 $ 메타 문자와는 달리 전체 문자열의 끝과 매치된다.

# \b
\b는 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분된다.

# 그루핑 ()
() 문자열이 계속해서 반복되는지 조사하는 정규식

```