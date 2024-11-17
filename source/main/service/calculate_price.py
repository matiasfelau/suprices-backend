from source.main.utility import logger
from source.main.utility.enum import LogTypes
from source.main.utility.exception import PriceException
from source.main.utility.logger import console_log


def calculate_price(market_price):
    """
    Calcula el precio de venta de un producto de Supermarket Together.
    :param market_price: Espera un float que represente en n decimales el precio de mercado del producto.
    :return: Devuelve un float que representa en dos decimales el precio de venta del producto.
    """
    try:
        console_log(LogTypes.INFO.value, f'Inicializando calculadora')
        maximized_price = maximize_price(market_price)
        return truncate_price(maximized_price)
    except PriceException:
        pass
    except Exception as e:
        console_log(LogTypes.ERROR.value, e)


def maximize_price(market_price):
    """
    Maximiza el precio de mercado de un producto de Supermarket Together en función de f : (0, ∞) → R, f(x) = 2x − 0.01
    que es la aceptación conocida de los clientes.
    :param market_price: Espera un float que represente en n decimales el precio de mercado del producto.
    :return: Devuelve un float que representa en n decimales el precio maximizado del producto.
    """
    try:
        console_log(LogTypes.INFO.value, f'Maximizando precio de mercado: {market_price}')
        return market_price * 2 - 0.01
    except Exception as e:
        console_log(LogTypes.ERROR.value, e)
        raise PriceException()


def truncate_price(maximized_price):
    """
    Trunca el precio maximizado de un producto de Supermarket Together en dos decimales.
    :param maximized_price: Espera un float que represente en n decimales el precio maximizado del producto.
    :return: Devuelve un float que representa en dos decimales el precio de venta del producto.
    """
    try:
        console_log(LogTypes.INFO.value, f'Truncando precio maximizado: {maximized_price}')
        return int(maximized_price * 100) / 100
    except Exception as e:
        console_log(LogTypes.ERROR.value, e)
        raise PriceException()
