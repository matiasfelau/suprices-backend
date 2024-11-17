import unittest

from util import logger
from util.enumeration import LogTypes


class LoggerTest(unittest.TestCase):


    def test_logging(self):
        logger.console_log(LogTypes.INFO.value,'El sistema de logeo está siendo probado')
        print("\n¿El resultado es correcto? (Y/N): ", end="")
        user_input = input().strip().upper()
        if user_input == "Y":
            print("Test validado por el usuario.", end="")
            self.assertTrue(True)  # Test pasa
        elif user_input == "N":
            print("Test rechazado por el usuario.", end="")
            self.fail("El usuario indicó que el resultado no es válido.")
        else:
            self.fail("Respuesta inválida.")

if __name__ == "__main__":
    unittest.main()