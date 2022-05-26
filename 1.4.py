def add_item(item_name, items_cost):
    global items, itemscost
    items.append(item_name)
    itemscost.append(int(items_cost))


def print_receipt():
    global items, itemscost, count
    if len(items) == 0:
        items.clear()
        itemscost.clear()
        return
    if len(items) != 0:
        print("Чек ", count, ". Всего предметов: ", len(items))
        count += 1
        sum = 0
        for i in range(0, len(items), 1):
            print(items[i], " - ", itemscost[i])
            sum += itemscost[i]
        print("Итого: ", sum)
        print("----")
        items.clear()
        itemscost.clear()



items = []
itemscost = []
count = 1

add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
