

class Request:

    def __init__(self, storages: list, request_str: str):
        self.storages = storages
        self.from_, self.to_, self.amount_, self.product_ = self._parse_request(request_str)

    def _parse_request(self, request_str):
        try:
            _, amount, product, _, from_, _, to = request_str.split()
            amount = int(amount)
            return from_, to, amount, product
        except (ValueError, TypeError):
            print('Не верный формат ввода запроса')
            return
