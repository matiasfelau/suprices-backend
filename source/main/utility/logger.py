import inspect
import os
from datetime import datetime, timezone, timedelta


def console_log(log_type, log_message):
    """

    :param log_type:
    :param log_message:
    :return:
    """
    try:
        current_time = get_current_time()
        log_origin = get_log_origin()
        print(f'\n[{current_time}] {log_type}: [{log_message}] IN [{log_origin}]', end="")
    except Exception as e:
        print(e)


def get_current_time():
    """

    :return:
    """
    try:
        current_time = datetime.now()  # Obtiene la fecha y la hora actuales.
        return current_time.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        raise Exception(e)


def get_log_origin():
    """

    :return:
    """
    try:
        caller_frame = inspect.stack()[2] # Obtiene la función que invocó al log desde el stack de ejecución.
        caller_file = caller_frame.filename # Obtiene el nombre del archivo que contiene a la función.
        project_root = os.path.dirname(os.path.abspath(__file__)) # Obtiene la ruta del proyecto.
        caller_path = os.path.relpath(caller_file, project_root) # Obtiene la ruta de la función dentro del proyecto.
        caller_name = caller_frame.function # Obtiene el nombre de la función.
        return f'{caller_path}::{caller_name}'
    except Exception as e:
        raise Exception(e)
