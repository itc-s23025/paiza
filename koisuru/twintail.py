s = int(input())  # 全体の長さ
t = int(input())  # 現在の進捗位置

progress = '-' * s  # 全体の長さ分のハイフンで構成された文字列を作成
progress = progress[:t-1] + '+' + progress[t:]  # 進捗位置に+を挿入

print(progress)

