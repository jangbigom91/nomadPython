# function 정의
# python에서 function의 body는 들여쓰기로 구분한다.
# function안의 body에 기능이 있어야 function이 제대로 작동
def say_hello():
  print("hello")
  print("bye")

say_hello() # function 실행 -> function 이름뒤에 ()

# function이 인자(값)들을 input 받았을 때
def say_hi(who):
  print("hi", who)
  print("goodbye", who)

say_hi("Harry")

def plus(a, b):
  print(a + b)

def minus(a, b):
  print(a - b)

plus(2, 5)
minus(2, 5)