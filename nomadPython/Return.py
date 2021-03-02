def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)

def mutiple(a, b):
  return a * b
  print("return is kill the function")
  # return된 이후 function 종료, print값은 출력되지 않는다.

result = mutiple(3, 5)
print(result)

# return을 사용할 경우 function을 실행할 때 function이 return된 값으로 치환된다.
# return을 사용하고 나면 그 function은 종료
# 한번에 하나의 값만 return 할 수 있다.