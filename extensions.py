import requests
import json


from conf import KEYS, HEADERS


class APIException(Exception):
    pass


class Requst():
    @staticmethod
    def get_price(_message):
        if len(_message) != 3:
            raise APIException('Неверное количество параметров!')
            return False
        try:
            val1 = KEYS[_message[0]]
        except KeyError:
            raise APIException(f'Такой валюты {val1} в списке нет!')
            return False
        try:
            val2 = KEYS[_message[1]]
        except KeyError:
            raise APIException(f'Такой валюты {val2} в списке нет!')
            return False
        amount = _message[2]
        try:
            tem = float(amount)
            if tem <= 0:
                raise APIException('Количество валюты должно быть положительным!')
                return False
        except ValueError:
            print('Третье значение не число!')
            return False

        url = f'https://api.apilayer.com/currency_data/convert?to={val2}&from={val1}&amount={amount}'
        r = requests.get(url, headers=HEADERS)
        try:
            result = json.loads(r.content)['result']
        except:
            print('Ошибка запроса. Закончился доступ к сайту...')
        return result


