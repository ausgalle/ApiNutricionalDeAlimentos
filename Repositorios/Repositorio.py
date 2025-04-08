import pyodbc;
from Entidades import Alimento;
from Utilidades import Configuracion;

class Repositorio:

	def ListarAlimentos(self) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

			consulta: str = """SELECT * FROM alimentos""";
			cursor = conexion.cursor();
			cursor.execute(consulta);

			for elemento in cursor:
				print(elemento);

			cursor.close();
			conexion.close();
		except Exception as ex:
			print(str(ex));
