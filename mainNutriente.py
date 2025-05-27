from Entidades.Alimento import Alimento
from Entidades.Nutriente import Nutriente
from Repositorios import Repositorio
from Repositorios import RepositorioNutriente
import hashlib
import binascii, os
import base64
from Crypto.Cipher import AES


# --- Main Program Logic ---
def main():
    repositorio = Repositorio.Repositorio()
    repositorio_nutriente = RepositorioNutriente.RepositorioNutriente()

    while True:
        print("\n--- Gestión de Nutrientes ---")
        print("1. Insertar Nutriente")
        print("2. Obtener Nutriente por ID")
        print("3. Listar Nutrientes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n--- Insertar Nuevo Nutriente (con encriptación) ---")

            nombre_nutriente_input = input("Ingrese el nombre del nutriente: ")

            unidad_medida_input = input("Ingrese la unidad de medida (ej. ml, mg, g): ")

            nutriente_a_insertar = Nutriente()
            nutriente_a_insertar.SetNombreNutriente(nombre_nutriente_input)
            nutriente_a_insertar.SetUnidadMedida(unidad_medida_input)

            try:
                repositorio_nutriente.InsertarNutriente(nutriente_a_insertar)
                print("Nutriente insertado (encriptado) exitosamente.")
            except Exception as e:
                print(f"Error al insertar nutriente: {e}")

        elif opcion == '2':
            print("\n--- Obtener Nutriente por ID (y descifrar) ---")
            try:
                nutriente_id = int(input("Ingrese el ID del nutriente a buscar: "))
                retrieved_nutriente = repositorio_nutriente.ObtenerNutrientePorId(nutriente_id)

                if retrieved_nutriente:
                   
                    print(f"Nutriente encontrado y descifrado:")
                    print(f"  ID: {retrieved_nutriente.GetIdNutriente()}")
                    print(f"  Nombre: {retrieved_nutriente.GetNombreNutriente()}")
                    print(f"  Unidad de Medida: {retrieved_nutriente.GetUnidadMedida()}")
                else:
                    print(f"No se encontró ningún nutriente con el ID {nutriente_id}.")
            except ValueError:
                print("ID inválido. Por favor, ingrese un número entero.")
            except Exception as e:
                print(f"Error al obtener o descifrar el nutriente: {e}")

        elif opcion == '3':
            # --- Obtener Nutriente por ID ---
            print("\n--- Obtener Nutrientes ---")
            try:
                repositorio_nutriente.ListarNutrientes()

            except Exception as e:
                print(f"Error al obtener o descifrar el nutriente: {e}")

        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()