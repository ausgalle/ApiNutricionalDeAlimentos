import pyodbc
from Entidades.Nutriente import Nutriente
from Entidades.NutrienteUnidad import NutrienteUnidad
from Utilidades import Configuracion
import hashlib;
import binascii, os;
import base64;
from Crypto.Cipher import AES;

datos_cifrados_estaticos = {
    'ciphertext': '1234567890abcdef1234567890abcdef',
    'nonce': '1234567890abcdef',
    'authTag': 'AWDSFASDFASDFASDFASDFASDFASDFASDF'
}

class EncriptarAESEstatico:

    # ¡PELIGRO! Esta clave está quemada en el código.
    # En una aplicación real, esto es INSEGURO.
    # Deberías usar un método más seguro para gestionar claves.
    secretKey = b'P3r4Gr1n0_S3gUr0_d3_32Byt3s_2025'

    def Cifrar(self, valor: str) -> str:
        # Asegurarse de que la clave tenga 32 bytes
        if len(self.secretKey) != 32:
            raise ValueError("La clave secreta debe tener 32 bytes.")
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(valor.encode('utf-8'))
        encrypted_data = b''.join([aesCipher.nonce, ciphertext, authTag])
        return base64.b64encode(encrypted_data).decode('utf-8')

    def Descifrar(self, valor_cifrado: str) -> str:
        # Asegurarse de que la clave tenga 32 bytes
        if len(self.secretKey) != 32:
            raise ValueError("La clave secreta debe tener 32 bytes.")
        encrypted_data = base64.b64decode(valor_cifrado)
        nonce = encrypted_data[:16]
        authTag = encrypted_data[-16:]
        ciphertext = encrypted_data[16:-16]

        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce=nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext.decode('utf-8')
        
class RepositorioNutriente:

    def ListarNutrientes(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_nutriente, nombre_nutriente, unidad_medida FROM nutrientes"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento);

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex));

    def ObtenerNutrientePorId(self, id_nutriente: int) -> Nutriente | None:
        nutriente = None
        seguridad_string = EncriptarAESEstatico();
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_nutriente, nombre_nutriente, unidad_medida FROM nutrientes WHERE id_nutriente = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (id_nutriente,))
            row = cursor.fetchone()

            if row:
                nutriente = Nutriente()
                nutriente.SetIdNutriente(row[0])
                print(row[1]);
                nombre_desencriptado = seguridad_string.Descifrar(row[1])
                nutriente.SetNombreNutriente(nombre_desencriptado)
                nutriente.SetUnidadMedida(row[2])

            print(nombre_desencriptado);
            cursor.close()
            conexion.close()
        except Exception as ex:
            print(f"Error al obtener nutriente por ID: {ex}")
        return nutriente

    def InsertarNutriente(self, nutriente: Nutriente) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor();
            segudidad_string = EncriptarAESEstatico();
            nutriente.SetNombreNutriente(segudidad_string.Cifrar(nutriente.GetNombreNutriente()));

            consulta: str = "{CALL proc_insert_nutriente(?, ?)}"
            parametros = (
                nutriente.GetNombreNutriente(),
                nutriente.GetUnidadMedida()
            )

            cursor.execute(consulta, parametros)
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print("Error al insertar nutriente:", str(ex))

    def ActualizarNutriente(self, nutriente: Nutriente) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """UPDATE nutrientes SET nombre_nutriente = ?, unidad_medida = ? WHERE id_nutriente = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (nutriente.GetNombreNutriente(), nutriente.GetUnidadMedida(), nutriente.GetIdNutriente()))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al actualizar nutriente: {ex}")
            return False

    def EliminarNutriente(self, id_nutriente: int) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """DELETE FROM nutrientes WHERE id_nutriente = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (id_nutriente,))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al eliminar nutriente: {ex}")
            return False

    def ListarNutrientesUnidades(self) -> list[NutrienteUnidad]:
        lista_nutrientes_unidades = []
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_nutriente_unidad, id_nutriente, id_unidad, es_default FROM nutrientes_unidades"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for row in cursor:
                nutriente_unidad = NutrienteUnidad()
                nutriente_unidad.SetIdNutrienteUnidad(row[0])
                nutriente_unidad.SetIdNutriente(row[1])
                nutriente_unidad.SetIdUnidad(row[2])
                nutriente_unidad.SetEsDefault(row[3])
                lista_nutrientes_unidades.append(nutriente_unidad)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(f"Error al listar nutrientes_unidades: {ex}")
        return lista_nutrientes_unidades

    def ObtenerNutrienteUnidadPorId(self, id_nutriente_unidad: int) -> NutrienteUnidad | None:
        nutriente_unidad = None
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_nutriente_unidad, id_nutriente, id_unidad, es_default FROM nutrientes_unidades WHERE id_nutriente_unidad = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (id_nutriente_unidad,))
            row = cursor.fetchone()

            if row:
                nutriente_unidad = NutrienteUnidad()
                nutriente_unidad.SetIdNutrienteUnidad(row[0])
                nutriente_unidad.SetIdNutriente(row[1])
                nutriente_unidad.SetIdUnidad(row[2])
                nutriente_unidad.SetEsDefault(row[3])

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(f"Error al obtener nutriente_unidad por ID: {ex}")
        return nutriente_unidad

    def InsertarNutrienteUnidad(self, nutriente_unidad: NutrienteUnidad) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta: str = "{CALL proc_insert_nutriente_unidad(?, ?, ?)}"
            parametros = (
                nutriente_unidad.GetIdNutriente(),
                nutriente_unidad.GetIdUnidad(),
                nutriente_unidad.GetEsDefault()
            )

            cursor.execute(consulta, parametros)
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print("Error al insertar nutriente_unidad:", str(ex))

    def ActualizarNutrienteUnidad(self, nutriente_unidad: NutrienteUnidad) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """UPDATE nutrientes_unidades SET id_nutriente = ?, id_unidad = ?, es_default = ? WHERE id_nutriente_unidad = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (nutriente_unidad.GetIdNutriente(), nutriente_unidad.GetIdUnidad(), nutriente_unidad.GetEsDefault(), nutriente_unidad.GetIdNutrienteUnidad()))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al actualizar nutriente_unidad: {ex}")
            return False

    def EliminarNutrienteUnidad(self, id_nutriente_unidad: int) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """DELETE FROM nutrientes_unidades WHERE id_nutriente_unidad = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (id_nutriente_unidad,))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al eliminar nutriente_unidad: {ex}")
            return False