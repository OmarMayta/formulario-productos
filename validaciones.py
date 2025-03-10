# Lista de categorías permitidas
CATEGORIAS_VALIDAS = ["Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"]

def validar_nombre(nombre):
    """ Valida que el nombre no supere los 20 caracteres. """
    return len(nombre) <= 20

def validar_precio(precio):
    """ Valida que el precio sea un número mayor a 0 y menor a 999. """
    return 0 < precio < 999

def validar_categorias(categorias):
    """ Valida que todas las categorías ingresadas estén en la lista permitida. """
    return all(categoria.strip() in CATEGORIAS_VALIDAS for categoria in categorias)

def validar_estado(estado):
    """ Valida que el estado del producto sea 'Si' o 'No'. """
    return estado in ["si", "no"]
