from Entidades.Alimento import Alimento
from Entidades.Nutriente import Nutriente
from Repositorios import Repositorio;
from Repositorios import RepositorioNutriente;

repositorio = Repositorio.Repositorio();


# # # Insertar alimento

# alimento = Alimento()
# alimento.SetNombreComun("BananaDos")
# alimento.SetNombreCientifico("Musa spp.")
# alimento.SetDescripcion("Fruta tropical rica en potasio.")
# alimento.SetTamanoPorcion(120.0)
# alimento.SetUnidadPorcion("gramos")
# alimento.SetImagenUrl("https://example.com/imagenes/banana.jpg")
# alimento.SetNotas("Perfecta para un snack energético.")

# repositorio.InsertarAlimento(alimento);


#Actualizar alimento

# alimento = Alimento()
# alimento.SetIdAlimento(1)  # ID del alimento que quieres actualizar
# alimento.SetNombreComun("Manzana")
# alimento.SetNombreCientifico("Musa spp.")
# alimento.SetDescripcion("Fruta tropical rica en potasio.")
# alimento.SetTamanoPorcion(120.0)
# alimento.SetUnidadPorcion("gramos")
# alimento.SetImagenUrl("https://example.com/imagenes/banana.jpg")
# alimento.SetNotas("Perfecta para un snack energético.")
# alimento.SetFechaCreacion("2023-01-01 12:00:00")

# repositorio.ActualizarAlimento(alimento)


# repositorio.EliminarAlimento(6)

#Listar alimentos
# repositorio.ListarAlimentos();


# # Insertar nutriente
repositorio_nutriente = RepositorioNutriente.RepositorioNutriente()
nutriente = Nutriente()
nutriente.SetNombreNutriente("Vitamina D")
nutriente.SetUnidadMedida("mg")
repositorio_nutriente.InsertarNutriente(nutriente)
print("Nutriente insertado.")





"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""