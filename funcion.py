def calcular_precio_final(precio: float, descuento: float) -> float:
    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero")

    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    precio_final = precio - (precio * descuento / 100)

    return round(precio_final, 2)
