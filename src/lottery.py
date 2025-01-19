import random

def draw_lottery():
    prizes = ['大当たり', '当たり', '小当たり', 'はずれ']
    result = random.choice(prizes)  # ランダムに結果を選ぶ
    return result

# くじを引く
result = draw_lottery()
print(f"結果: {result}")