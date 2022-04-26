class can:
    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso

    


if __name__ == "__main__":
    perrito = can("Tatiana", 7)
    perrito.nombre = "Roxy"
    perrito.peso = 4
    print(f"El perro se llama {perrito.nombre}, pesa {perrito.peso} kg")