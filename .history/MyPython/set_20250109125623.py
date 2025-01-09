s1 = {1, 2, 3, "tuple"}
s2 = list(s1)
s3 = {"a:1", "b:2", "c:3", "d:tuple"}

print(s3)
print(type(s3))
print(s1)
print(type(s1))
print(s2)
print(type(s2))


a = ["sato", "suzuki", "takahashi", "tanaka", "watanabe"]
# a = [1,2,3,4,5]
j = 0
for i in a:

    # print(a[i])
    j += 1
    print(j, "番目", i)

print("全員で", j, "人です。")
