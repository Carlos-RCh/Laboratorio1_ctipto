from scapy.all import ICMP, Raw, sys, rdpcap
from colorama import Fore

texto = ""

def descifrar_cesar(texto_cifrado, corrimiento):
    texto_descifrado = ""
    for char in texto_cifrado:
        if char.isalpha():
            if char.islower():
                nuevo_char = chr((ord(char) - ord('a') - corrimiento) % 26 + ord('a'))
            else:
                nuevo_char = chr((ord(char) - ord('A') - corrimiento) % 26 + ord('A'))
            texto_descifrado += nuevo_char
        else:
            texto_descifrado += char
    return texto_descifrado

# Función para procesar los paquetes ICMP recibidos
def procesar_paquete(paquete):
    global texto
    if ICMP in paquete and paquete[ICMP].type == 8:
        # Obtener el payload del paquete ICMP
        payload = paquete[Raw].load.hex()

        # Obtener el carácter cifrado
        caracter_cifrado = payload[:2]

        texto += chr(int(caracter_cifrado, 16))


archivo_pcap = input("Ingrese el archivo: ")

# Cargar el archivo pcapng
paquetes = rdpcap(archivo_pcap)

# Iterar sobre cada paquete del archivo
for paquete in paquetes:
    procesar_paquete(paquete)

for i in range(26):
    cesar = descifrar_cesar(texto, i)
    if cesar == "criptografia y seguridad en redes":
        print(Fore.GREEN + f'{i}  {cesar}')
    else:
        print(Fore.WHITE + f'{i}  {cesar}')




