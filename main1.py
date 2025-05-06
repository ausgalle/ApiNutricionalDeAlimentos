from Entidades.Alimento import Alimento
from Entidades.Nutriente import Nutriente
from Repositorios import Repositorio;
from Repositorios import RepositorioNutriente;
import hashlib;
import binascii, os;
import base64;
from Crypto.Cipher import AES;


# class Seguridad:
#     secretKey = os.urandom(32);

#     def Cifrar(self, valor: str) -> str:
#         aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
#         ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(valor));
#         return (ciphertext, aesCipher.nonce, authTag);

#     def Descifrar(self, valor: str) -> str:
#         (ciphertext, nonce, authTag) = valor;
#         aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
#         plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
#         return plaintext;

class EncriptarAES:

    secretKey = os.urandom(32)

    def Cifrar(self, valor: str) -> str:
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(valor.encode('utf-8'))
        # Concatenamos nonce, ciphertext y authTag, y luego lo codificamos en base64 para obtener un string
        encrypted_data = b''.join([aesCipher.nonce, ciphertext, authTag])
        return base64.b64encode(encrypted_data).decode('utf-8')

    def Descifrar(self, valor_cifrado: str) -> str:
        encrypted_data = base64.b64decode(valor_cifrado)
        nonce = encrypted_data[:16]  # El nonce siempre tiene 16 bytes
        authTag = encrypted_data[-16:] # El auth tag siempre tiene 16 bytes
        ciphertext = encrypted_data[16:-16]

        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce=nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext.decode('utf-8')

repositorio = Repositorio.Repositorio();
# seguridad = EncriptarAES();

# # Listar nutrientes
repositorio_nutriente = RepositorioNutriente.RepositorioNutriente();

# Insertar nutriente encriptado
nutriente_a_insertar = Nutriente();
valor = "VITAMINA ED";
nutriente_a_insertar.SetNombreNutriente(valor);
nutriente_a_insertar.SetUnidadMedida("ml");
# repositorio_nutriente.InsertarNutriente(nutriente_a_insertar);
repositorio_nutriente.ObtenerNutrientePorId(9);
print("Nutriente insertado (encriptado).");




"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""