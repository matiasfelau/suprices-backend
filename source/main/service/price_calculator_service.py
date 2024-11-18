from source.main.utility.enumeration import LogTypes
from source.main.utility.exception import PriceException, CalculatorException
from source.main.utility.logger import console_log


def calculate_price(market_price):
    """
    Calcula el precio de venta de un producto de Supermarket Together.
    :param market_price: Espera un float que represente en n decimales el precio de mercado del producto.
    :return: Devuelve un float que representa en dos decimales el precio de venta del producto.
    """
    console_log(LogTypes.INFO, f'Calculando el precio...')
    try:
        maximized_price = maximize_price(market_price)
        trucated_price = truncate_price(maximized_price)
        console_log(LogTypes.INFO, 'El precio fue calculado exitosamente')
        return trucated_price
    except PriceException as e:
        message = str(e)
        console_log(LogTypes.WARNING, 'La calculadora no pudo finalizar el procesamiento')
        raise PriceException(message)
    except Exception as e:
        message = str(e)
        console_log(LogTypes.ERROR, message)
        raise CalculatorException(message)


def maximize_price(market_price):
    """
    Maximiza el precio de mercado de un producto de Supermarket Together en función de f : (0, ∞) → R, f(x) = 2x − 0.01
    que es la aceptación conocida de los clientes.
    :param market_price: Espera un float que represente en n decimales el precio de mercado del producto.
    :return: Devuelve un float que representa en n decimales el precio maximizado del producto.
    """
    console_log(LogTypes.INFO, f'Maximizando precio de mercado: {market_price}')
    try:
        return market_price * 2 - 0.01
    except Exception as e:
        message = str(e)
        console_log(LogTypes.ERROR, message)
        raise PriceException(message)


def truncate_price(maximized_price):
    """
    Trunca el precio maximizado de un producto de Supermarket Together en dos decimales.
    :param maximized_price: Espera un float que represente en n decimales el precio maximizado del producto.
    :return: Devuelve un float que representa en dos decimales el precio de venta del producto.
    """
    console_log(LogTypes.INFO, f'Truncando precio maximizado: {maximized_price}')
    try:
        return int(maximized_price * 100) / 100
    except Exception as e:
        message = str(e)
        console_log(LogTypes.ERROR, message)
        raise PriceException(message)
