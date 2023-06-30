amount = int(input())
def calculate_points(amount):
    points = amount // 100  # 100円毎に付与されるポイント
    if amount >= 1000:
        points += 10  # ボーナスポイントの追加
    print(points)
calculate_points(amount)

