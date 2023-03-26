from entitys.base import Storage
from entitys.request import Request
from entitys.shop import Shop
from entitys.store import Store


def main():

    store = Store()
    shop = Shop()

    while True:
        print('Введите запрос на перемещение товаров(например, "Доставить 3 печеньки из склад в магазин"):')
        request_str = input()

        request = Request([store, shop], request_str)

# if __name__ == "__main__":
