import time
import random

preparados_espera = random.randint(1,3)
time.sleep(preparados_espera)
print("preparados")

listos_espera = random.randint(1,3)
time.sleep(listos_espera)
print("listos")

ya_espera = random.randint(1,5)
time.sleep(ya_espera)
inicio = time.time()
x = input("YA!")
fin = time.time()

reaccion = fin - inicio
print("Tu tiempo de reaccion ha sido", reaccion)


