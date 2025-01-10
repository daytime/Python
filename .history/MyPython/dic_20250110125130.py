d = {"リンゴ": 10, "オレンジ": 20, "バナナ": 30}  # -
e = dict(リンゴ=10, オレンジ=20, バナナ=30)  # -
f = dict([["リンゴ", 10], ["オレンジ", 20], ["バナナ", 30]])  # -
print("d ", d)
print("d = ", type(d))  # -
print("e ", e)
print("e = ", type(e))  # -
print("f ", f)
print("f = ", type(f))  # -

d = {"リンゴ": 10, "オレンジ": 20, "バナナ": 30, "リンゴ": 40}  # -
print("d ", d)
print(d.keys())
print(d.values())
