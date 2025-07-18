import random
import time
from datetime import datetime

def rolldice():
    return random.randint(1, 6)  # Retorna um número aleatório entre 1 e 6

def welcome_message():
    print("Bem-vindo ao projeto Python K8s! Esta aplicação simula o lançamento de um dado.")

print("Hello from Kubernetes!")
welcome_message()

while True:
    time.sleep(10)  # Pausa de 10 segundos
    #now = datetime.now()
    #formatted = now.strftime("%Y-%m-%d %H-%M-%S")        
    print(f"Rolando o dado... Resultado: {rolldice()}")