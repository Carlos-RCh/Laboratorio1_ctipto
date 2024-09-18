
def cifrado_cesar(texto, corrimiento): # funcion algoritmo de cesar.
    texto_cifrado = ""

    for char in texto:
        
        if char.isupper(): # Verifica letra mayúsculas 
            texto_cifrado += chr((ord(char) + corrimiento - 65) % 26 + 65)
        
        elif char.islower(): # Verifica letra minúscula
            texto_cifrado += chr((ord(char) + corrimiento - 97) % 26 + 97)
        else:
            
            texto_cifrado += char

    return texto_cifrado


texto_a_cifrar = input("Ingrese el texto a cifrar: ")
corrimiento = int(input("Ingrese el corrimiento: "))    


texto_cifrado = cifrado_cesar(texto_a_cifrar, corrimiento)
print(f"Texto cifrado: {texto_cifrado}")







# criptografia y seguridad en redes
# larycxpajorj h bnpdarmjm nw anmnb