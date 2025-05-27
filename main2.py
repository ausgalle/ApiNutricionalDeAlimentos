from Entidades.Alimento import Alimento
from Entidades.Nutriente import Nutriente
from Entidades.ComposicionNutricional import ComposicionNutricional
from Repositorios import Repositorio
from Repositorios import RepositorioNutriente

repositorio = Repositorio.Repositorio()
repositorio_nutriente = RepositorioNutriente.RepositorioNutriente()

def insertar_alimento():
    alimento = Alimento()
    alimento.SetNombreComun(input("Nombre común: "))
    alimento.SetNombreCientifico(input("Nombre científico: "))
    alimento.SetDescripcion(input("Descripción: "))
    alimento.SetTamanoPorcion(float(input("Tamaño porción (número): ")))
    alimento.SetUnidadPorcion(input("Unidad porción: "))
    alimento.SetImagenUrl(input("URL de imagen: "))
    alimento.SetNotas(input("Notas: "))
    
    repositorio.InsertarAlimento(alimento)
    print("✅ Alimento insertado.")

def actualizar_alimento():
    alimento = Alimento()
    alimento.SetIdAlimento(int(input("ID del alimento a actualizar: ")))
    alimento.SetNombreComun(input("Nuevo nombre común: "))
    alimento.SetNombreCientifico(input("Nuevo nombre científico: "))
    alimento.SetDescripcion(input("Nueva descripción: "))
    alimento.SetTamanoPorcion(float(input("Nuevo tamaño porción: ")))
    alimento.SetUnidadPorcion(input("Nueva unidad porción: "))
    alimento.SetImagenUrl(input("Nueva URL de imagen: "))
    alimento.SetNotas(input("Nuevas notas: "))
    alimento.SetFechaCreacion(input("Fecha creación (YYYY-MM-DD HH:MM:SS): "))

    repositorio.ActualizarAlimento(alimento)
    print("✅ Alimento actualizado.")

def eliminar_alimento():
    id_alimento = int(input("ID del alimento a eliminar: "))
    repositorio.EliminarAlimento(id_alimento)
    print("✅ Alimento eliminado.")

def listar_alimentos():
    alimentos = repositorio.ListarAlimentos()
    # for a in alimentos:
    #     print(a)

def insertar_nutriente():
    nutriente = Nutriente()
    nutriente.SetNombreNutriente(input("Nombre del nutriente: "))
    nutriente.SetUnidadMedida(input("Unidad de medida: "))
    repositorio_nutriente.InsertarNutriente(nutriente)
    print("✅ Nutriente insertado.")

def listar_nutrientes():
    nutrientes = repositorio_nutriente.ListarNutrientes()
    for n in nutrientes:
        print(n)

def insertar_composicion():
    composicion = ComposicionNutricional()
    composicion.SetIdAlimento(int(input("ID del alimento: ")))
    composicion.SetIdNutriente(int(input("ID del nutriente: ")))
    composicion.SetCantidad(float(input("Cantidad: ")))
    composicion.SetValorDiarioPorcentaje(float(input("Valor diario (%): ")))
    composicion.SetNotas(input("Notas: "))
    
    resultado = repositorio.InsertarComposicion(composicion)
    print("✅ Resultado de la inserción:", resultado)

def actualizar_composicion():
    composicion = ComposicionNutricional()
    composicion.SetIdComposicion(int(input("ID de la composición a actualizar: ")))
    composicion.SetIdAlimento(int(input("Nuevo ID del alimento: ")))
    composicion.SetIdNutriente(int(input("Nuevo ID del nutriente: ")))
    composicion.SetCantidad(float(input("Nueva cantidad: ")))
    composicion.SetValorDiarioPorcentaje(float(input("Nuevo valor diario (%): ")))
    composicion.SetNotas(input("Nuevas notas: "))

    resultado = repositorio.ActualizarComposicion(composicion)
    print("✅ Resultado de la actualización:", resultado)

def eliminar_composicion():
    id_composicion = int(input("ID de la composición a eliminar: "))
    repositorio.EliminarComposicion(id_composicion)
    print("✅ Composición eliminada.")

def listar_composiciones():
    composiciones = repositorio.ListarComposiciones()

def listar_categorias():
    categorias = repositorio.ListarCategorias()

def menu():
    while True:
        print("\n📋 MENÚ PRINCIPAL")
        print("1. Insertar alimento")
        print("2. Actualizar alimento")
        print("3. Eliminar alimento")
        print("4. Listar alimentos")
        print("5. Insertar nutriente")
        print("6. Listar nutrientes")
        print("7. Insertar composición nutricional")
        print("8. Actualizar composición nutricional")
        print("9. Eliminar composición nutricional")
        print("10. Listar composiciones nutricionales")
        print("11. Listar categorías de alimento")
        print("12. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar_alimento()
        elif opcion == "2":
            actualizar_alimento()
        elif opcion == "3":
            eliminar_alimento()
        elif opcion == "4":
            listar_alimentos()
        elif opcion == "5":
            insertar_nutriente()
        elif opcion == "6":
            listar_nutrientes()
        elif opcion == "7":
            insertar_composicion()
        elif opcion == "8":
            actualizar_composicion()
        elif opcion == "9":
            eliminar_composicion()
        elif opcion == "10":
            listar_composiciones()
        elif opcion == "11":
            listar_categorias()
        elif opcion == "12":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
