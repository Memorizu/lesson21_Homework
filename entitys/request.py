
class Request:

    def __init__(self, storages: list, request_str: str):
        try:
            self.storages = storages
            self.from_, self.to_, self.amount_, self.product_ = self._parse_request(request_str)
        except Exception as e:
            print(f'Неверный формат ввода {e}')
            self.from_, self.to_, self.amount_, self.product_ = None, None, None, None

    def _parse_request(self, request_str):
        try:
            _, amount, product, _, from_, _, to = request_str.split()
            amount = int(amount)
            return from_, to, amount, product
        except (ValueError, TypeError):
            print('Не верный формат ввода запроса')
            return None, None, None, None
