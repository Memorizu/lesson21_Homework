from abc import ABC


class Storage(ABC):

    def __init__(self, capacity: int):
        self._items = {}
        self._capacity = capacity

    def add(self, title, quantity):
        if quantity < self._capacity:
            self._items[title] = self._items.get(title, 0) + quantity
            self._capacity -= quantity
        else:
            print("Не хватает места на складе")
            return

    def remove(self, title, quantity):
        if not self.check_item(title=title):
            return 'Такого товара нет'
        if self._items[title] > quantity:
            self._items[title] = self._items.get(title, 0) - quantity
            self._capacity += quantity
        else:
            return f'Не достаточно количества. Доступно {self._items[title]}.'

    def get_free_space(self):
        return self._capacity

    def get_items(self):
        return self._items

    def get_item_count(self, title):
        return self._items[title]

    def get_unique_item_count(self):
        return len(set(self._items.keys()))

    def check_item(self, title):
        return title in self._items

    @property
    def output(self):
        return '\n'.join([f'{v} {k}' for k, v in self._items.items()])
