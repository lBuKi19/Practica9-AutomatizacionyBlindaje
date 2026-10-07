import pytest

from funcion import calcular_precio_final


def test_calcular_precio_con_descuento():
    # Arrange
    precio = 1000
    descuento = 20
    resultado_esperado = 800

    # Act
    resultado_obtenido = calcular_precio_final(precio, descuento)

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_calcular_precio_sin_descuento():
    # Arrange
    precio = 1000
    descuento = 0
    resultado_esperado = 1000

    # Act
    resultado_obtenido = calcular_precio_final(precio, descuento)

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_calcular_precio_con_descuento_total():
    # Arrange
    precio = 1000
    descuento = 100
    resultado_esperado = 0

    # Act
    resultado_obtenido = calcular_precio_final(precio, descuento)

    # Assert
    assert resultado_obtenido == resultado_esperado


def test_precio_cero_lanza_error():
    # Arrange
    precio = 0
    descuento = 20
    mensaje_esperado = "El precio debe ser mayor que cero"

    # Act
    with pytest.raises(ValueError) as error:
        calcular_precio_final(precio, descuento)

    # Assert
    assert str(error.value) == mensaje_esperado


def test_precio_negativo_lanza_error():
    # Arrange
    precio = -500
    descuento = 20
    mensaje_esperado = "El precio debe ser mayor que cero"

    # Act
    with pytest.raises(ValueError) as error:
        calcular_precio_final(precio, descuento)

    # Assert
    assert str(error.value) == mensaje_esperado


def test_descuento_negativo_lanza_error():
    # Arrange
    precio = 1000
    descuento = -10
    mensaje_esperado = "El descuento debe estar entre 0 y 100"

    # Act
    with pytest.raises(ValueError) as error:
        calcular_precio_final(precio, descuento)

    # Assert
    assert str(error.value) == mensaje_esperado


def test_descuento_mayor_a_cien_lanza_error():
    # Arrange
    precio = 1000
    descuento = 110
    mensaje_esperado = "El descuento debe estar entre 0 y 100"

    # Act
    with pytest.raises(ValueError) as error:
        calcular_precio_final(precio, descuento)

    # Assert
    assert str(error.value) == mensaje_esperado
