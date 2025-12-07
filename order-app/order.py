import sys

class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name}: ¥{self.price}"

food1 = Menu("ショートケーキ", 600)
food2 = Menu("チョコケーキ", 700)
food3 = Menu("モンブラン", 750)
foods = [food1, food2, food3]

drink1 = Menu("コーヒー", 500)
drink2 = Menu("紅茶", 600)
drink3 = Menu("緑茶", 450)
drinks = [drink1, drink2, drink3]

def new_order():
    food_index = 1
    print("===メニューを選んでください===")
    for food in foods:
        print(f"{str(food_index)}. {food.info()}")
        food_index += 1
    order_food = int(input("注文番号："))
    if order_food < 1 or order_food > 3:
        print("--------------------")
        print("無効な選択です")
        sys.exit()
    order_food -= 1
    drink_index = 1
    print()
    print("===セットドリンクを選んでください===")
    for drink in drinks:
        print(f"{str(drink_index)}. {drink.info()}")
        drink_index += 1
    order_drink = int(input("注文番号："))
    if order_drink < 1 or order_drink > 3:
        print("--------------------")
        print("無効な選択です")
        sys.exit()
    order_drink -= 1
    result = foods[order_food].price + drinks[order_drink].price
    print()
    print("===注文内容===")
    print(foods[order_food].info())
    print(drinks[order_drink].info())
    print()
    print(f"合計金額: ¥{str(result)}")

new_order()