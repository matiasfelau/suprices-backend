import inspect
import os
from datetime import datetime, timezone, timedelta

from colorama import Style, Fore

from source.main.utility.enumeration import LogTypes


def console_log(log_type, log_message):
    """
    Imprime un log en la terminal
    :param log_type: Elemento de utility.enumeration.LogTypes
    :param log_message:
    :return:
    """
    try:
        color = get_log_color(log_type)
        current_time = get_current_time()
        log_origin = get_log_origin()
        print(color + f'\n[{current_time}] {log_type}: [{log_message}] IN [{log_origin}]' + Style.RESET_ALL, end="")
    except Exception as e:
        print(str(e))


def get_log_color(log_type):
    """
    Asigna un color al log en base a su tipo
    :param log_type:
    :return: Elemento de Fore
    """
    try:
        if log_type == LogTypes.INFO:
            return Fore.GREEN
        elif log_type == LogTypes.WARNING:
            return Fore.YELLOW
        elif log_type == LogTypes.ERROR:
            return Fore.RED
        else:
            raise Exception(f'Tipo de log inválido: {log_type}')
    except Exception as e:
        raise Exception(str(e))


def get_current_time():
    """

    :return: Devuelve la fecha y la hora actuales
    """
    try:
        current_time = datetime.now()  # Obtiene la fecha y la hora actuales.
        return current_time.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        raise Exception(str(e))


def get_log_origin():
    """

    :return: Devuelve la ruta al metodo invocador
    """
    try:
        caller_frame = inspect.stack()[2] # Obtiene la función que invocó al log desde el stack de ejecución.
        caller_file = caller_frame.filename # Obtiene el nombre del archivo que contiene a la función.
        project_root = os.path.dirname(os.path.abspath(__file__)) # Obtiene la ruta del proyecto.
        caller_path = os.path.relpath(caller_file, project_root) # Obtiene la ruta de la función dentro del proyecto.
        caller_name = caller_frame.function # Obtiene el nombre de la función.
        return f'{caller_path}::{caller_name}'
    except Exception as e:
        raise Exception(str(e))
