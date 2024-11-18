import unittest

from source.main.utility import logger
from source.main.utility.enumeration import LogTypes


class LogTest(unittest.TestCase):


    def test_log(self):
        logger.console_log(LogTypes.INFO.value, 'El sistema de registros está siendo probado')
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