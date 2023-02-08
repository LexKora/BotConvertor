import requests
import json


from conf import KEYS, HEADERS, SPELLING


class APIException(Exception):
    pass


class Requst():
    @staticmethod
    def get_price(_message):
        if len(_message) != 3:
            raise APIException('Неверное количество параметров!')

        try:
            val1 = KEYS[_message[0]]
        except KeyError:
            raise APIException(f'Такой валюты {_message[0]} в списке нет!')

        try:
            val2 = KEYS[_message[1]]
        except KeyError:
            raise APIException(f'Такой валюты {_message[1]} в списке нет!')

        amount = _message[2]
        try:
            tem = float(amount)
            if tem <= 0:
                raise APIException('Количество валюты должно быть положительным числом!')
        except ValueError:
            raise APIException('Количество валюты должно числом!')

        url = f'https://api.apilayer.com/currency_data/convert?to={val2}&from={val1}&amount={amount}'
        r = requests.get(url, headers=HEADERS)
        try:
            result = json.loads(r.content)['result']
        except ValueError:
            print('Ошибка запроса. Отсутствует доступ к сайту...')

        return result


def _spelling(val, num):
    if 5 <= num <= 20:
        return SPELLING[val][0]
    elif num % 10 == 1:
        return SPELLING[val][1]
    elif num % 10 in (2, 3, 4):
        return SPELLING[val][2]
    else:
        return SPELLING[val][0]

