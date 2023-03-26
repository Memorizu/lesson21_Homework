from entitys.base import Storage


class Store(Storage):
    def __init__(self, capacity=100):
        super().__init__(capacity)

    def add(self, title, quantity):
        super().add(title=title, quantity=quantity)

    def remove(self, title, quantity):
        super().remove(title=title, quantity=quantity)
        return f'Забрали со склада {title} - {quantity}'



# store = Store()
# store.add('fish', 3)
# store.add('bread', 4)
# store.add('oil', 5)
# store.add('oil', 6)
# store.add('oil', 7)
#
# print(store.get_items())
# store.remove('bread', 10)
# print(store.get_items())
# print(store.remove('oil', 13))
# print(store.get_items())
# print(store.get_unique_item_count())
# print(store.get_free_space())
