from entitys.base import Storage


class Shop(Storage):
    def __init__(self, capacity=20):
        super().__init__(capacity)
        self._max_items = 5

    def add(self, title, quantity):
        if len(self._items) >= self._max_items:
            print('Магазин переполнен')
            return
        super().add(title=title, quantity=quantity)

    def remove(self, title, quantity):
        if len(self._items) >= self._max_items:
            return 'Укажите меньшее количество'
        elif title not in self._items:
            return'Такого товара нет'
        super().remove(title=title, quantity=quantity)



# shop = Shop()
# shop.add('матрешка', 3)
# shop.add('vanilla', 4)
# shop.add('cup', 2)
# shop.remove('cup', 1)
# print(shop.get_items())
# print(shop.get_unique_item_count())

