from Entidades.Alimento import Alimento
from Repositorios import Repositorio;

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
alimento = Alimento()
alimento.SetIdAlimento(1)  # ID del alimento que quieres actualizar
alimento.SetNombreComun("Banana")
alimento.SetNombreCientifico("Musa spp.")
alimento.SetDescripcion("Fruta tropical rica en potasio.")
alimento.SetTamanoPorcion(120.0)
alimento.SetUnidadPorcion("gramos")
alimento.SetImagenUrl("https://example.com/imagenes/banana.jpg")
alimento.SetNotas("Perfecta para un snack energético.")
alimento.SetFechaCreacion("2023-01-01 12:00:00")

# Llamar al método para actualizar el alimento
repositorio.ActualizarAlimento(alimento)



#Listar alimentos
repositorio.ListarAlimentos();





"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""