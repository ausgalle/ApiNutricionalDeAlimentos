from Entidades.Alimento import Alimento
import pyodbc;
from Utilidades import Configuracion;
import datetime

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
   
	def InsertarAlimento(self, alimento: Alimento) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
			cursor = conexion.cursor()

			consulta: str = "{CALL proc_insert_alimento(?, ?, ?, ?, ?, ?, ?, ?,?)}"
			parametros = (
				alimento.GetNombreComun(),
				alimento.GetNombreCientifico(),
				alimento.GetDescripcion(),
				alimento.GetTamanoPorcion(),
				alimento.GetUnidadPorcion(),
				alimento.GetImagenUrl(),
				alimento.GetNotas(),
				datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # fecha_creacion
   				datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			)

			cursor.execute(consulta, parametros)
			conexion.commit()

			cursor.close()
			conexion.close()
		except Exception as ex:
			print("Error al insertar alimento:", str(ex))
