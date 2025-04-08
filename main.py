import datetime 
from Repositorios import Repositorio;

repositorio = Repositorio.Repositorio();
# repositorio.InsertBasico("Test 3");
# repositorio.InsertarPersona("9784551", "usme", 1, datetime.datetime.now(), 1)
repositorio.ListarAlimentos();

"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""
