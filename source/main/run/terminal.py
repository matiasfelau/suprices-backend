from source.main.service.calculate_price import calcular_precio

if __name__ == '__main__':
    print('Esta aplicación te permitirá maximizar el precio de un producto de Supermarket Together a partir de su precio de mercado.', end="")
    while True:
        precio_mercado = float(input('\nIngresá el precio de mercado del producto: '))
        precio_venta = calcular_precio(precio_mercado)
        print(f'El precio de venta es: {precio_venta}', end="")
