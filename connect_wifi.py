import os
import time

def connect_to_wifi(ssid, password):
    # Aqui entra a lógica real de conectar o Wi-Fi.
    # Exemplo: printar que está tentando conectar.
    print(f"Tentando conectar na rede: {ssid}")
    time.sleep(2)
    print("Conectado com sucesso!")

if __name__ == "__main__":
    ssid = os.getenv('WIFI_SSID', 'MinhaRedePadrao')
    password = os.getenv('WIFI_PASSWORD', 'SenhaPadrao')
    
    connect_to_wifi(ssid, password)
