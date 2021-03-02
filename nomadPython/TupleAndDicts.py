# 수정 불가능한 list -> tuple()
days = ("Mon","Tue","Wed","Thur","Fri")
print(type(days))

# Dictionary -> {}로 표현
nico = {
  "name" : "Nico",
  "age" : 31,
  "korean" : True,
  "fav_fodd" : ["Pizza", "Sushi"]
}
print(nico)
nico["gender"] = "Men"
print(nico)