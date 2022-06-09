# 파이썬의 OOT


## 📖 파이썬의 OOT
파이썬은 객체 지향적 언어로도 사용이 가능하다.




파이썬은 함수는 다음과 같이 선언이 가능하다.

```
def add_num(a: int, b: int) ->int:
    return a + b

# 들어오는 매개변수 a, b 가 int형이고 반환값이 int형이다
라는 의미이다.
```

단 여기서 a, b의 값을 "a" "b"를 넣어줄 경우 값이 
"ab"가 리턴 되는데 아마 표기상으로 타입을 표시하는것으로 이해하면 된다.


```
def menu(entree, drink, dessert):
    pass

같은 함수가 있을경우 
menu(a,b,c) 로 넣을수도 있으나 각각의 매개변수 넣은 값을
조정하여 넣을수도 있는데 그 방법은 다음과 같다.

menu(entree = "a", drink = "b", dessert = "c")
```
단 여기서 만약에 몇개는 지정해줬는데 중간에 지정안한 경우 즉 
menu(drink ="b", "a", dessert = "c") 같은 경우에는 에러를 유발시키니 조심하자!

📖  함수의 디폴트 값을 정해줄수도 있다.

```
def menu(entree, drink = "b", dessert="c"):
    pass

menu("a")
```
아무값도 넘겨주지 않을 경우에는 디폴트값이 들어간다. 여기서 제일 중요한 점은 list 같은 값들은 절때 디폴트값으로 사용해선 안된다!

📖  위치인수를 튜플화 시킬수도 있다.
```
def menu(*argc):
    for arg in args:
        print(arg)

menu("a", "b", "c")

=====================
a
b
c
```
이 특성은 튜플의 패킹과 언패킹을 사용하는 특징을 이용 한 것이다.

📖  이번에는 사전화 시켜서 넘겨주는 방법이다.
```
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

menu(entree = "a", brink = "b", dessert = "c")

=====================
entree a
brink b
dessert c
```
와 같이 **dic 으로 묶어주게 되면 사전형으로 들어가서 값을 조정할 수 있다.

📖  함수의 주석을 다는 방법은 다음과 같다.

```
def menu(**kwargs):
    """ 
    안녕하세요 여기에 주석을 달아주시면 됩니다.
    """
    for k, v in kwargs.items():
        print(k, v)

menu(entree = "a", brink = "b", dessert = "c")
```
함수의 밖에서 사용해도 되나 이렇게 작성하는것이 제일 깔끔하며 보기 좋다.


📖 함수 내의 함수
```
def outer(a, b):
    def plus(c, d):
        return c + d
    r = plus(a,b)
    print(r)

outer(1,2)
======
3
```
함수 안에서 함수를 지정하여서 사용할 수 있다.

📖 클로저

```
def outer(a, b):
    def inner():
        return a + b

    return inner

outer(1, 2)

f = outer(1, 2)
r = f()
print(r)
======
3
```
클로저 기법은 다음과 같다. def outer을 거친 inner 함수로 덮혀진 객체 하나가 나온다. 이는 아직 패킹되어 있으므로 f()을 통해서 패킹을 풀어주고 그 값을 print 한다는 의미 이다.

📖 제네레이터

```
def greeting():
    yield "good moning"
    yield "good aternoon"
    yield "good night"

g = greeting()
print(next(g))

```
yield 을 통해서 next로 조절을 하여 사용한다.
만약 돌려줄 yield가 없을 경우 stop error 을 발생 시킨다.

📖 데코레이터

```
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
@trace    # @데코레이터
def hello():
    print('hello')
 
@trace    # @데코레이터
def world():
    print('world')
 
hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출
============================================
hello 함수 시작
hello
hello 함수 끝
world 함수 시작
world
world 함수 끝
```
데코레이터 다음에 함수가 오며, 해당 함수를 wrapper(): 내에서 사용할 수가 있다.
참고로 데코레이터에 걸려서 온 func에 매개변수가 포함이 되어 있다면, 이를 wrapper(*args, **kwargs) 를 사용하여 매개변수 또한 가져올 수 있다.


<br>


## ⊙ 파이썬의 함수
