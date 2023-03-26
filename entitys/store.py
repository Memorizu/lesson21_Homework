from entitys.base import Storage


class Store(Storage):
    def __init__(self, capacity=100):
        super().__init__(capacity)

    def add(self, title, quantity):
        super().add(title=title, quantity=quantity)

    def remove(self, title, quantity):
        super().remove(title=title, quantity=quantity)
        return f'Забрали со склада {title} - {quantity}'
