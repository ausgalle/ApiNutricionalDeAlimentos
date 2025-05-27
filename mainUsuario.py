from Entidades.Usuario import Usuario
from Repositorios.RepositorioUsuario import RepositorioUsuario

# --- Main Program Logic ---
def main():
    repositorio_usuario = RepositorioUsuario()

    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Insertar Usuario")
        print("2. Obtener Usuario por ID")
        print("3. Listar Nurtrientes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # --- Insertar Usuario ---
            print("\n--- Insertar Nuevo Usuario (con encriptación) ---")
            try:
                nombre_usuario = input("Ingrese el nombre de usuario: ")
                contrasena = input("Ingrese la contraseña: ")
                email = input("Ingrese el email: ")
                id_rol = input("Ingrese el ID del rol (opcional, Enter si no aplica): ")

                usuario = Usuario()
                usuario.SetNombreUsuario(nombre_usuario)
                usuario.SetContrasena(contrasena)
                usuario.SetEmail(email)

                if id_rol.strip().isdigit():
                    usuario.SetIdRol(int(id_rol))

                repositorio_usuario.InsertarUsuario(usuario)
                print("Usuario insertado exitosamente.")

            except Exception as e:
                print(f"Error al insertar usuario: {e}")

        elif opcion == '2':
            # --- Obtener Usuario por ID ---
            print("\n--- Obtener Usuario por ID (y descifrar) ---")
            try:
                usuario_id = int(input("Ingrese el ID del usuario a buscar: "))
                usuario_recuperado = repositorio_usuario.ObtenerUsuarioPorId(usuario_id)

                if usuario_recuperado:
                    print(f"\nUsuario encontrado:")
                    print(f"  ID: {usuario_recuperado.GetIdUsuario()}")
                    print(f"  Nombre: {usuario_recuperado.GetNombreUsuario()}")
                    print(f"  Contraseña: {usuario_recuperado.GetContrasena()}")
                    print(f"  Email: {usuario_recuperado.GetEmail()}")
                    print(f"  ID Rol: {usuario_recuperado.GetIdRol()}")
                    print(f"  Fecha Registro: {usuario_recuperado.GetFechaRegistro()}")
                    print(f"  Último Login: {usuario_recuperado.GetUltimoLogin()}")
                    print(f"  Activo: {'Sí' if usuario_recuperado.GetActivo() else 'No'}")
                else:
                    print(f"No se encontró ningún usuario con el ID {usuario_id}.")

            except ValueError:
                print("ID inválido. Por favor, ingrese un número entero.")
            except Exception as e:
                print(f"Error al obtener o descifrar el usuario: {e}")

        elif opcion == '2':
            # --- Obtener Usuario por ID ---
            print("\n--- Lista de nutrientes ---")
            try:
                usuario_recuperado = repositorio_usuario.ListarUsuarios()

            except Exception as e:
                print(f"Error al obtener usuarios {e}")

        elif opcion == '4':
            # --- Salir ---
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
