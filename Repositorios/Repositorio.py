from Entidades.Alimento import Alimento
import pyodbc;
from Utilidades import Configuracion;
import datetime

class Repositorio:
    
    
	# Alimentos
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
   
   
	def ActualizarAlimento(self, alimento: Alimento) -> None:
		try:
			# Establece la conexión con la base de datos
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
			cursor = conexion.cursor()

			# Consulta para actualizar el alimento usando un procedimiento almacenado
			consulta: str = "{CALL proc_update_alimento(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}"
			
			# Parámetros para la actualización
			parametros = (
				alimento.GetIdAlimento(),  # ID del alimento a actualizar
				alimento.GetNombreComun(),
				alimento.GetNombreCientifico(),
				alimento.GetDescripcion(),
				alimento.GetTamanoPorcion(),
				alimento.GetUnidadPorcion(),
				alimento.GetImagenUrl(),
				alimento.GetNotas(),
				datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # fecha_actualizacion
				alimento.GetFechaCreacion()  # se mantiene la fecha de creación
			)

			# Ejecuta la consulta
			cursor.execute(consulta, parametros)
			conexion.commit()  # Confirma los cambios

			cursor.close()
			conexion.close()

			print("Alimento actualizado correctamente.")

		except Exception as ex:
			print("Error al actualizar alimento:", str(ex))
   
   
	def EliminarAlimento(self, id_alimento: int) -> None:
		try:
			# Establece la conexión con la base de datos
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
			cursor = conexion.cursor()

			# Consulta para eliminar un alimento usando un procedimiento almacenado
			consulta: str = "{CALL proc_delete_alimento(?)}"

			# Parámetros para la eliminación
			parametros = (id_alimento,)

			# Ejecuta la consulta
			cursor.execute(consulta, parametros)
			conexion.commit()  # Confirma los cambios

			cursor.close()
			conexion.close()

			print("Alimento eliminado correctamente.")

		except Exception as ex:
			print("Error al eliminar alimento:", str(ex))
