# Keyword Argument
# 인자의 위치에 상관없이 인자의 이름에 따라 결정
def plus(a, b):
  return a + b

result = plus(b=30, a=1)
print(result)

def say_hello(name, age):
  return f"Hello {name} you are {age} years old"

hello = say_hello(age="12", name="nico")
print(hello)

def say_hi(name, age, gender):
  return "Hello " + name + " you are" + age + " years old and a " + gender

hi = say_hi(gender="men", name="nico", age="22")
print(hi)

def plus(a, b):
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return None

print(plus(12,1.2))