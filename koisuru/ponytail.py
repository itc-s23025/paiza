answers = []
for _ in range(5):
    d, e = input().split()
    answers.append((d, e))

correct_count = sum(answer[0] == answer[1] for answer in answers)

if correct_count >= 3:
    print("OK")
else:
    print("NG")

