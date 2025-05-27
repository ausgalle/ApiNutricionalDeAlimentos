from Entidades.Alimento import Alimento
from Entidades.Nutriente import Nutriente
from Entidades.ComposicionNutricional import ComposicionNutricional
from Repositorios import Repositorio;
from Repositorios import RepositorioNutriente;

repositorio = Repositorio.Repositorio();


# # Insertar alimento

# alimento = Alimento()
# alimento.SetNombreComun("Peras2")
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


# # Listar nutrientes por ID
# repositorio_nutriente = RepositorioNutriente.RepositorioNutriente();
# # repositorio_nutriente.ObtenerNutrientePorId(1);

# # Insertar nutriente
# repositorio_nutriente = RepositorioNutriente.RepositorioNutriente()
# nutriente = Nutriente()
# nutriente.SetNombreNutriente("Vitamina D")    
# nutriente.SetUnidadMedida("mg")
# repositorio_nutriente.InsertarNutriente(nutriente)
# print("Nutriente insertado.")

# # Listar nutrientes
# repositorio_nutriente = RepositorioNutriente.RepositorioNutriente();
# repositorio_nutriente.ListarNutrientes();


# repositorio.ListarComposiciones();

# composicion = ComposicionNutricional()
# composicion.SetIdAlimento(1)
# composicion.SetIdNutriente(1)
# composicion.SetCantidad(12.5)
# composicion.SetValorDiarioPorcentaje(30.0)
# composicion.SetNotas("Ejemplo de inserción manual")

# resultado = repositorio.InsertarComposicion(composicion)
# print("Resultado de la inserción:", resultado)


# composicion = ComposicionNutricional()
# composicion.SetIdComposicion(3)
# composicion.SetIdAlimento(1)
# composicion.SetIdNutriente(1)
# composicion.SetCantidad(15.0)  # Cambias cantidad, por ejemplo
# composicion.SetValorDiarioPorcentaje(35.0)
# composicion.SetNotas("Ejemplo de actualización")

# resultado = repositorio.ActualizarComposicion(composicion)
# print("Resultado de la actualización:", resultado)

# repositorio.EliminarComposicion(5)

repositorio.ListarCategorias()







"""
VERSION DE PYTHON
py -3 --version
EJECUTAR
py main.py

DEPENDENCIAS, NUGETS, PAQUETES
py -m pip install pyodbc
"""