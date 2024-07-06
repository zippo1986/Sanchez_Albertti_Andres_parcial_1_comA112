def validar_entero(numero:str):
    """_summary_
    Valida que el numero pasado por str sea enttero

    Args:
        numero (str): recibe un numero en str

    Returns:
        _type_: retorna true o false
    """
    for i in numero:
        try:
            int(i)
            return True
        except ValueError:
            return False
def validar_genero(genero):
    """_summary_
    valida el genero ingresado por el usuario a partir de una lista

    Args:
        genero (str): el genero buscado por el usuario

    Returns:
        bool: retorna True si encuentra el genero en la lista
    """
    lista_generos=["terror","comedia","drama","accion"]
    for g in lista_generos:
        if genero ==g:
            return True
        
        
    