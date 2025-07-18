# app.py
import random  # Importa o módulo random
import time    # Importa o módulo time

def rolldice():
    return random.randint(1, 6)  # Retorna um número aleatório entre 1 e 6

print("Hello from Kubernetes! v0.1.1")

while True:
    time.sleep(10)  # Pausa de 10 segundos        
    print(f"Rolando o dado... Resultado: {rolldice()}")