import pyodbc
from Entidades.Usuario import Usuario
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

    secretKey = b'P3r4Gr1n0_S3gUr0_d3_32Byt3s_2025'

    def Cifrar(self, valor: str) -> str:
        if len(self.secretKey) != 32:
            raise ValueError("La clave secreta debe tener 32 bytes.")
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(valor.encode('utf-8'))
        encrypted_data = b''.join([aesCipher.nonce, ciphertext, authTag])
        return base64.b64encode(encrypted_data).decode('utf-8')

    def Descifrar(self, valor_cifrado: str) -> str:
        if len(self.secretKey) != 32:
            raise ValueError("La clave secreta debe tener 32 bytes.")
        encrypted_data = base64.b64decode(valor_cifrado)
        nonce = encrypted_data[:16]
        authTag = encrypted_data[-16:]
        ciphertext = encrypted_data[16:-16]

        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce=nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext.decode('utf-8')
        

class RepositorioUsuario:

    def ListarUsuarios(self) -> None:
        lista_usuarios = []
        seguridad_string = EncriptarAESEstatico();
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_usuario, nombre_usuario, contrasena, email, id_rol, fecha_registro, ultimo_login, activo FROM usuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for row in cursor:
                usuario = Usuario() 
                usuario.SetIdUsuario(row[0])
                usuario.SetNombreUsuario(row[1])
                try:
                    usuario.SetContrasena(self.seguridad_string.Descifrar(row[2]))
                except Exception as dec_pass_ex:
                    print(f"Advertencia: No se pudo descifrar la contraseña para el usuario ID {row[0]}. Error: {dec_pass_ex}")
                    usuario.SetContrasena(f"ERROR_CIFRADO_PASS:{row[2]}") # Store raw encrypted for debugging
                try:
                    usuario.SetEmail(self.seguridad_string.Descifrar(row[3]))
                except Exception as dec_email_ex:
                    print(f"Advertencia: No se pudo descifrar el email para el usuario ID {row[0]}. Error: {dec_email_ex}")
                    usuario.SetEmail(f"ERROR_CIFRADO_EMAIL:{row[3]}") # Store raw encrypted for debugging
                
                usuario.SetIdRol(row[4])
                usuario.SetFechaRegistro(row[5].strftime("%Y-%m-%d %H:%M:%S") if isinstance(row[5], datetime) else row[5]) # Format datetime object
                usuario.SetUltimoLogin(row[6].strftime("%Y-%m-%d %H:%M:%S") if isinstance(row[6], datetime) else row[6]) # Format datetime object
                usuario.SetActivo(bool(row[7]))
                lista_usuarios.append(usuario)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(f"Error al listar usuarios: {ex}")
        return lista_usuarios
        

    def ObtenerUsuarioPorId(self, id_usuario: int) -> None:
        usuario = None
        seguridad_string = EncriptarAESEstatico();
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """
                SELECT 
                    id_usuario, 
                    nombre_usuario, 
                    contrasena, 
                    email, 
                    id_rol, 
                    fecha_registro, 
                    ultimo_login, 
                    activo 
                FROM usuarios 
                WHERE id_usuario = ?
            """

            cursor = conexion.cursor()
            cursor.execute(consulta, (id_usuario,))
            row = cursor.fetchone()

            if row:
                usuario = Usuario()
                usuario.SetIdUsuario(row[0])
                usuario.SetNombreUsuario(row[1])

                try:
                    usuario.SetContrasena(seguridad_string.Descifrar(row[2]))
                except Exception as dec_pass_ex:
                    print(f"Advertencia: No se pudo descifrar la contraseña para el usuario ID {row[0]}. Error: {dec_pass_ex}")
                    usuario.SetContrasena(f"ERROR_CIFRADO_{row[2]}")

                try:
                    usuario.SetEmail(seguridad_string.Descifrar(row[3]))
                except Exception as dec_email_ex:
                    print(f"Advertencia: No se pudo descifrar el email para el usuario ID {row[0]}. Error: {dec_email_ex}")
                    usuario.SetEmail(f"ERROR_CIFRADO_{row[3]}")

                usuario.SetIdRol(row[4])
                usuario.SetFechaRegistro(row[5].strftime("%Y-%m-%d %H:%M:%S") if row[5] else None)
                usuario.SetUltimoLogin(row[6].strftime("%Y-%m-%d %H:%M:%S") if row[6] else None)
                usuario.SetActivo(bool(row[7]))

            cursor.close()
            conexion.close()

        except Exception as ex:
            print(f"Error al obtener usuario por ID: {ex}")

        return usuario

    def InsertarUsuario(self, usuario: Usuario) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor();
            seguridad_string = EncriptarAESEstatico();

            encrypted_contrasena = seguridad_string.Cifrar(usuario.GetContrasena())
            encrypted_email = seguridad_string.Cifrar(usuario.GetEmail())

            consulta: str = "{CALL proc_insert_usuario(?, ?, ?, ?)}"
            parametros = (
                usuario.GetNombreUsuario(),
                encrypted_contrasena,
                encrypted_email,
                usuario.GetIdRol()
            )

            cursor.execute(consulta, parametros)
            conexion.commit()

            cursor.close()
            conexion.close()
            print("Usuario insertado exitosamente.")
        except Exception as ex:
            print(f"Error al insertar usuario: {ex}")

    def ActualizarUsuario(self, usuario: Usuario) -> bool:
        seguridad_string = EncriptarAESEstatico();
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            encrypted_contrasena = self.seguridad_string.Cifrar(usuario.GetContrasena())
            encrypted_email = self.seguridad_string.Cifrar(usuario.GetEmail())

            consulta: str = """
                UPDATE usuarios SET 
                nombre_usuario = ?, 
                contrasena = ?, 
                email = ?, 
                id_rol = ?, 
                ultimo_login = ?, 
                activo = ? 
                WHERE id_usuario = ?
            """
            parametros = (
                usuario.GetNombreUsuario(),
                encrypted_contrasena,
                encrypted_email,
                usuario.GetIdRol(),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Update last login on update
                usuario.GetActivo(),
                usuario.GetIdUsuario()
            )
            cursor.execute(consulta, parametros)
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al actualizar usuario: {ex}")
            return False
