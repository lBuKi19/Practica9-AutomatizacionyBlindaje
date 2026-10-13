DESCUENTO_PREMIUM = 10


def validar_compra(
    precio: float,
    descuento: float,
    usuario_activo: bool,
    stock: int,
) -> str | None:
    if not usuario_activo:
        return "Error: el usuario está inactivo"

    if stock <= 0:
        return "Error: no hay stock disponible"

    if precio <= 0:
        return "Error: el precio debe ser mayor que cero"

    if descuento < 0:
        return "Error: el descuento no puede ser negativo"

    if descuento > 100:
        return "Error: el descuento no puede superar 100"

    return None


def aplicar_descuento(precio: float, porcentaje: float) -> float:
    return precio - (precio * porcentaje / 100)


def procesar_compra(
    precio: float,
    descuento: float,
    usuario_activo: bool,
    cliente_premium: bool,
    stock: int,
) -> str:
    error = validar_compra(
        precio,
        descuento,
        usuario_activo,
        stock,
    )

    if error is not None:
        return error

    precio_final = aplicar_descuento(precio, descuento)

    if cliente_premium:
        precio_final = aplicar_descuento(
            precio_final,
            DESCUENTO_PREMIUM,
        )
        tipo_cliente = "premium"
    else:
        tipo_cliente = "estándar"

    return f"Compra {tipo_cliente} autorizada por ${precio_final:.2f}"
