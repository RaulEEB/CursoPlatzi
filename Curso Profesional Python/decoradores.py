def decordor(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

@decordor
def saludo():
    print("Hola Antonio.")

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(text):
    return f'{text}, recibiste un mensaje!!!'


if __name__ == '__main__':
    saludo()
    print(mensaje("Raúl"))
