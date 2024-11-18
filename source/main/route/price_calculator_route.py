from flask import Blueprint, request, jsonify

from source.main.service import price_calculator_service
from source.main.utility.check import is_float, is_positive
from source.main.utility.enumeration import LogTypes
from source.main.utility.exception import PriceException, CalculatorException, BadRequestException, ValidationException
from source.main.utility.logger import console_log

calculate_price_route = Blueprint('calculate_price_route', __name__)


@calculate_price_route.route('/calculator', methods=['POST'])
def calculate_price():
    """
    Controla solicitudes para calcular el precio de venta de un producto de Supermarket Together a partir del precio de
    mercado.
    :return:
    """
    console_log(LogTypes.INFO, 'Petición recibida para calcular un nuevo precio')
    try:
        received_data = request.get_json()
        market_price = validate_price_calculator_received_data(received_data)
        new_price = price_calculator_service.calculate_price(market_price)
        console_log(LogTypes.INFO, f'La solicitud se procesó correctamente')
        return jsonify({'new_price': new_price}), 200
    except BadRequestException as e:
        message = str(e)
        console_log(LogTypes.WARNING, 'La solicitud fue rechazada')
        return jsonify({'error': f'{message}'}), 400
    except (PriceException, CalculatorException, ValidationException) as e:
        message = str(e)
        console_log(LogTypes.WARNING, 'La solicitud no se procesó correctamente')
        return jsonify({'error': f'{message}'}), 500
    except Exception as e:
        message = str(e)
        console_log(LogTypes.ERROR, message)
        return jsonify({'error': f'{message}'}), 500

def validate_price_calculator_received_data(received_data):
    console_log(LogTypes.INFO, 'Validando la solicitud recibida...')
    try:
        if 'market_price' not in received_data:
            raise BadRequestException('La solicitud no contiene el campo: "market_price"')
        market_price = received_data['market_price']
        if not is_float(market_price):
            raise BadRequestException(f'El valor: {market_price} no es de tipo float')
        if not is_positive(market_price):
            raise BadRequestException(f'El valor: {market_price} no es un número positivo')
        console_log(LogTypes.INFO, 'La solicitud superó con éxito las validaciones')
        return market_price
    except BadRequestException as e:
        message = str(e)
        console_log(LogTypes.WARNING, 'La solicitud no superó con éxito las validaciones')
        raise BadRequestException(message)
    except Exception as e:
        message = str(e)
        console_log(LogTypes.ERROR, message)
        raise ValidationException(message)