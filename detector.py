
import time
from collections import defaultdict
from alerta import enviar_alerta

acessos = defaultdict(list)

def verificar_ameaca(ip):
    agora = time.time()
    acessos[ip].append(agora)

    acessos[ip] = [t for t in acessos[ip] if agora - t < 60]

    if len(acessos[ip]) > 3:
        enviar_alerta(f"ALERTA: IP {ip} com mais de 3 acessos em 1 minuto!")
        return f"Alerta gerado para IP {ip}."

    return "Acesso normal."
