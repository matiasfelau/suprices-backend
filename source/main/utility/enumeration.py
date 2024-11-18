from enum import Enum


class LogTypes(Enum):
    """

    """
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'


    def __str__(self):
        """
        Permite acceder al valor del elemento invocado
        :return:
        """
        return self.value
