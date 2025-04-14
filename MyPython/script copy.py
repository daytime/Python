print("リストの練習")
scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 90, "社会": 85}
science = scores["理科"]
society = scores["社会"]
difference = science - society
print("理科は社会より " + str(difference) + " 点高いです。")


scores_values = list(scores.values())
avg_score = sum(scores_values) / len(scores_values)
for score_name, score in scores.items():

    print(score_name + "は" + str(score) + "点です。")
