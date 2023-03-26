from entitys.request import Request
from entitys.shop import Shop
from entitys.store import Store


def main():

    store = Store()
    shop = Shop()

    store.add('печеньки', 10)
    store.add('конфеты', 10)
    store.add('хлеб', 10)
    store.add('молоко', 10)
    shop.add('сигареты', 4)

    while True:
        print('Введите запрос на перемещение товаров(например, "Доставить 3 печеньки из склад в магазин"):')
        request_str = input()

        request = Request([store, shop], request_str)
        if request.from_ == 'склад' and request.to_ == 'магазин':
            if store.check_item(request.product_):
                if store.get_item_count(request.product_) >= request.amount_:
                    store.remove(request.product_, request.amount_)
                    print(f'Курьер забрал {request.amount_} {request.product_} со склада в магазин.')
                    shop.add(request.product_, request.amount_)
                    print(f'Курьер доставил {request.amount_} {request.product_} в магазин')
                    print(f'На складе хранится: \n\n{store.output}')
                    print(f'В магазине хранится: \n\n{shop.output}\n')
                else:
                    print(f'Не достаточно количества на складе. Доступно {store.get_item_count(request.product_)}')
            else:
                print('Такого товара нет на складе')
        if request.from_ == 'магазин' and request.to_ == 'склад':
            if shop.check_item(request.product_):
                if shop.get_item_count(request.product_) >= request.amount_:
                    shop.remove(request.product_, request.amount_)
                    print(f'Курьер забрал {request.amount_} {request.product_} из магазина на склад.')
                    store.add(request.product_, request.amount_)
                    print(f'Курьер доставил {request.product_} {request.amount_} на склад')
                    print(f'На складе хранится: \n\n{store.output}')
                    print(f'В магазине хранится: \n\n{shop.output}\n')
                else:
                    print(f'Недостаточно количества в магазине. Доступно {shop.get_item_count(request.product_)}')
            else:
                print('Такого товара нет в магазине.')


if __name__ == "__main__":
    main()
