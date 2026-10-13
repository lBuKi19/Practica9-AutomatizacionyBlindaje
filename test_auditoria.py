from auditoria import procesar_compra


def test_compra_estandar_autorizada():
    # Arrange
    precio = 1000
    descuento = 20
    usuario_activo = True
    cliente_premium = False
    stock = 5
    resultado_esperado = "Compra estándar autorizada por $800.00"

    # Act
    resultado_obtenido = procesar_compra(
        precio,
        descuento,
        usuario_activo,
        cliente_premium,
        stock,
    )

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_compra_premium_autorizada():
    # Arrange
    precio = 1000
    descuento = 20
    usuario_activo = True
    cliente_premium = True
    stock = 5
    resultado_esperado = "Compra premium autorizada por $720.00"

    # Act
    resultado_obtenido = procesar_compra(
        precio,
        descuento,
        usuario_activo,
        cliente_premium,
        stock,
    )

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_usuario_inactivo():
    # Arrange
    precio = 1000
    descuento = 20
    usuario_activo = False
    cliente_premium = False
    stock = 5
    resultado_esperado = "Error: el usuario está inactivo"

    # Act
    resultado_obtenido = procesar_compra(
        precio,
        descuento,
        usuario_activo,
        cliente_premium,
        stock,
    )

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_compra_sin_stock():
    # Arrange
    precio = 1000
    descuento = 20
    usuario_activo = True
    cliente_premium = False
    stock = 0
    resultado_esperado = "Error: no hay stock disponible"

    # Act
    resultado_obtenido = procesar_compra(
        precio,
        descuento,
        usuario_activo,
        cliente_premium,
        stock,
    )

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_precio_invalido():
    # Arrange
    precio = 0
    descuento = 20
    usuario_activo = True
    cliente_premium = False
    stock = 5
    resultado_esperado = "Error: el precio debe ser mayor que cero"

    # Act
    resultado_obtenido = procesar_compra(
        precio,
        descuento,
        usuario_activo,
        cliente_premium,
        stock,
    )

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_descuento_negativo():
    # Arrange
    precio = 1000
    descuento = -10
    usuario_activo = True
    cliente_premium = False
    stock = 5
    resultado_esperado = "Error: el descuento no puede ser negativo"

    # Act
    resultado_obtenido = procesar_compra(
        precio,
        descuento,
        usuario_activo,
        cliente_premium,
        stock,
    )

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_descuento_mayor_a_cien():
    # Arrange
    precio = 1000
    descuento = 110
    usuario_activo = True
    cliente_premium = False
    stock = 5
    resultado_esperado = "Error: el descuento no puede superar 100"

    # Act
    resultado_obtenido = procesar_compra(
        precio,
        descuento,
        usuario_activo,
        cliente_premium,
        stock,
    )

    # Assert
    assert resultado_obtenido == resultado_esperado
