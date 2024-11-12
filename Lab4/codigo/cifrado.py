from Crypto.Cipher import DES, AES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


# Funciones de algoritmo DES:
def adjust_key_DES(key):
    # Rellenar con bytes aleatorios si key < 8 bytes o truncar
    if len(key) < 8:
        key += get_random_bytes(8 - len(key))
    elif len(key) > 8:        
        key = key[:8]
    print(f"DES clave ajustada: {key}")
    return key

def encrypt_DES(key, iv, plaintext):
    # inicalizar cifrado de  DES 
    cipher = DES.new(key, DES.MODE_CBC, iv)

    # Verificar si el padding es necesario
    if len(plaintext) % DES.block_size != 0:
        padded_text = pad(plaintext.encode(), DES.block_size)
    else:
        padded_text = plaintext.encode() 

    encrypted_text = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode()

def des_decrypt(key, iv, ciphertext):
    # inicalizar descifrado de  DES 
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted_text = base64.b64decode(ciphertext)
    decrypted_text = cipher.decrypt(encrypted_text)
    
    # Verificar si es necesario remover el padding
    if len(decrypted_text) % DES.block_size == 0 and decrypted_text[-1] <= DES.block_size:
        unpadded_text = unpad(decrypted_text, DES.block_size)  # Remover padding si corresponde
    else:
        unpadded_text = decrypted_text 
    
    return unpadded_text.decode()





# Funciones de algoritmo AES-256:
def adjust_key_AES(key):
    # Rellenar con bytes aleatorios si key < 32 bytes o truncar
    if len(key) < 32:
        key += get_random_bytes(32 - len(key)) 
    elif len(key) > 32:
        key = key[:32] 
    print(f"AES clave ajustada: {key}")
    return key

def encrypt_AES(key, iv, plaintext):
    # inicalizar cifrado de AES 
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Verificar si el padding es necesario
    if len(plaintext) % AES.block_size != 0:
        padded_text = pad(plaintext.encode(), AES.block_size)
    else:
        padded_text = plaintext.encode()  

    encrypted_text = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode()


def decrypt_AES(key, iv, ciphertext):
    # inicalizar descifrado de AES
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_text = base64.b64decode(ciphertext)
    decrypted_text = cipher.decrypt(encrypted_text)
    
    # Verificar si es necesario remover el padding
    if len(decrypted_text) % AES.block_size == 0 and decrypted_text[-1] <= AES.block_size:
        unpadded_text = unpad(decrypted_text, AES.block_size)  
    else:
        unpadded_text = decrypted_text 
    
    return unpadded_text.decode()


# Funciones de algoritmo 3-DES:


def adjust_key_3DES(key):
    # Rellenar o truncar clave
    if len(key) < 24:
        key += get_random_bytes(24 - len(key))  
    elif len(key) > 24:
        key = key[:24] 
    print(f"3DES clave ajustada: {key}")
    return key

def encrypt_3DES(key, iv, plaintext):
    # inicalizar cripto
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    
    # Verificar si el padding es necesario
    if len(plaintext) % DES3.block_size != 0:
        padded_text = pad(plaintext.encode(), DES3.block_size)
    else:
        padded_text = plaintext.encode()  
    encrypted_text = cipher.encrypt(padded_text)
    
    return base64.b64encode(encrypted_text).decode()

def decrypt_3DES(key, iv, ciphertext):
    # inicalizar descripto
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    encrypted_text = base64.b64decode(ciphertext)
    decrypted_text = cipher.decrypt(encrypted_text)
    
    # Verificar si es necesario remover el padding
    if len(decrypted_text) % DES3.block_size == 0 and decrypted_text[-1] <= DES3.block_size:
        unpadded_text = unpad(decrypted_text, DES3.block_size)  
    else:
        unpadded_text = decrypted_text  
    
    return unpadded_text.decode()




def main():
    
    # Datos DES 
    
    print("Datos de entrada algoritmo DES:")
    key_DES = input("Ingresa la clave (mínimo 8 caracteres): ").encode()
    iv_DES = input("Ingresa el vector de inicialización (IV) (8 caracteres): ").encode()
    plaintext_DES = input("Ingresa el texto a cifrar: ")


    # Datos AES-256
    print("Datos de entrada algoritmo AES-256:")
    key_AES = input("Ingresa la clave (mínimo 32 caracteres): ").encode()
    iv_AES = input("Ingresa el vector de inicialización (IV) (16 caracteres): ").encode()
    plaintext_AES = input("Ingresa el texto a cifrar: ")


    # Datos 3 DES 
    print("Datos de entrada algoritmo 3DES:")
    key_3DES = input("Ingresa la clave (mínimo 24 caracteres): ").encode()
    iv_3DES = input("Ingresa el vector de inicialización (IV) (8 caracteres): ").encode()
    plaintext_3DES = input("Ingresa el texto a cifrar: ")

    
    
    key_DES = adjust_key_DES(key_DES)
    encrypted_text_DES = encrypt_DES(key_DES, iv_DES, plaintext_DES)
    print(f"Texto cifrado DES: {encrypted_text_DES}")
    decrypted_text = des_decrypt(key_DES, iv_DES, encrypted_text_DES)
    print(f"Texto descifrado DES: {decrypted_text}")


    key_AES = adjust_key_AES(key_AES)
    encrypted_text_AES = encrypt_AES(key_AES, iv_AES, plaintext_AES)
    print(f"Texto cifrado AES-256: {encrypted_text_AES}")
    decrypted_text = decrypt_AES(key_AES, iv_AES, encrypted_text_AES)
    print(f"Texto descifrado AES-256: {decrypted_text}")

    key_3DES = adjust_key_3DES(key_3DES)
    encrypted_text_3DES = encrypt_3DES(key_3DES, iv_3DES, plaintext_3DES)
    print(f"Texto cifrado 3DES: {encrypted_text_3DES}")
    decrypted_text = decrypt_3DES(key_3DES, iv_3DES, encrypted_text_3DES)
    print(f"Texto descifrado 3DES: {decrypted_text}")



if __name__ == "__main__":
    main()

# tatooinechewbacamustafar
# abababab
# mandalormandalormandalor

# tatooine
# chewbaca
# mustafar

#b8eRpfI9WdUGdGUT6JO28XCIwlYqUwih


