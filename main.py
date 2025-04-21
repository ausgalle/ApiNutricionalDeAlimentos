from Entidades.Alimento import Alimento
from Repositorios import Repositorio;

repositorio = Repositorio.Repositorio();


# alimento = Alimento()
# alimento.SetNombreComun("BananaDos")
# alimento.SetNombreCientifico("Musa spp.")
# alimento.SetDescripcion("Fruta tropical rica en potasio.")
# alimento.SetTamanoPorcion(120.0)
# alimento.SetUnidadPorcion("gramos")
# alimento.SetImagenUrl("https://example.com/imagenes/banana.jpg")
# alimento.SetNotas("Perfecta para un snack energético.")

# repositorio.InsertarAlimento(alimento);
repositorio.ListarAlimentos();


"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""