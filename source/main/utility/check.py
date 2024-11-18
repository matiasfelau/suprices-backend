from source.main.utility.enumeration import LogTypes
from source.main.utility.logger import console_log


def is_float(value):
    """
    Valida que el valor ingresado sea de tipo float
    :param value:
    :return: Devuelve True o False
    """
    console_log(LogTypes.INFO, f'Validando que el valor: {value} sea de tipo float')
    try:
        float(value)
        console_log(LogTypes.INFO, f'El valor: {value} es de tipo float')
        return True
    except ValueError:
        console_log(LogTypes.WARNING, f'El valor: {value} no es de tipo float')
        return False


def is_positive(value):
    """
    Valida que el valor ingresado sea positivo
    :param value:
    :return: Devuelve True o False
    """
    console_log(LogTypes.INFO, f'Validando que el valor: {value} sea un número positivo')
    if value > 0:
        console_log(LogTypes.INFO, f'El valor: {value} es un número positivo')
        return True
    else:
        console_log(LogTypes.WARNING, f'El valor: {value} no es un número positivo')
        return False