print("こんにちは！")
strawberry = 150
apple_price = 120
print(type(apple_price))
print(apple_price)
print(apple_price + strawberry)

apple_price = "120円"
print(type(apple_price))
print(apple_price)
# print(apple_price + strawberry)

apple_price = 100
name = "斎藤"
weight = 54.5
print(apple_price, name, weight)
print("apple_price = ", type(apple_price))
print("name = ", type(name))
print("weight = ", type(weight))

first_name = "斎藤"
last_name = "太郎"
honorific_name = "さん"
print(first_name + last_name + honorific_name + "です")
full_name = first_name + last_name + honorific_name
print(full_name + "様")

math = 82
japanese = 74
english = 60
avg_score = (math + japanese + english) / 3
print(avg_score)
print("avg_score" + atr(type(avg_score)))
print("平均点は" + str(avg_score) + "点です")
