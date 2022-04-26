from datetime import datetime
from multiprocessing.connection import wait

#Cuanto tiempo tarda en ejecutarse una función
def execution_time(func):
    def wrapper(*args, **kwargs):
        iniitial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - iniitial_time
        print("Pasaron " + str(round(time_elapsed.total_seconds(),2)) + " segundos.")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass



@execution_time
def suma(a: int, b: int)-> int:
    return a + b

@execution_time
def saludo(nombre="Antonio"):
    print(f"Hola, {nombre}")

suma(5,5)
random_func()
saludo("Raúl")