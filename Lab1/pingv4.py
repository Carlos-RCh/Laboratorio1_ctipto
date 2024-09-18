from scapy.all import send, IP, ICMP, Raw
import os
import sys
import time

# Loopback IP
ip_loopback = '127.0.0.1'

def convert_payload(data, index):
    icmp_data = bytes(data, 'utf-8') + os.urandom(1) + bytes([index])
    icmp_data += bytes('\x00\x00\x00\x00\x00\x00', 'utf-8')
    icmp_data += bytes(range(0x10, 0x38))

    return icmp_data

def enviar_icmp(payload_data, index):
    paquete = IP(src=ip_loopback, dst=ip_loopback)/ICMP(type=8, id=1, seq=index)/Raw(load=payload_data)
    send(paquete)
    time.sleep(1)


texto = input("Ingrese el texto: ")

for i in range(len(texto)):
    caracter = texto[i]
    payload_full = convert_payload(caracter, i)
    enviar_icmp(payload_full, i)
