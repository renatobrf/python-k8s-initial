import random
import time
from datetime import datetime

# The mount path as defined in your Pod's volumeMounts
#pvc_mount_path = "data"
pvc_mount_path = "/tmp"

def rolldice():
    return random.randint(1, 6)  # Retorna um número aleatório entre 1 e 6

def welcome_message():
    print("Bem-vindo ao projeto Python K8s! Esta aplicação simula o lançamento de um dado.")

welcome_message()

while True:
    time.sleep(10)  # Pausa de 10 segundos
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H-%M-%S")            
    resultado = f"{formatted} - Rolando o dado... Resultado: {rolldice()}"
    print(resultado)
    # Salva o resultado no arquivo dentro do PVC
    with open(pvc_mount_path+"/resultado.txt", "a") as f:  # Salva no PVC
        f.write(resultado + "\n")