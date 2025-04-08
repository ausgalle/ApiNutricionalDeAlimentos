import pyodbc;
from Entidades import Estados;
from Utilidades import Configuracion;
import datetime;

class Repositorio:

	def ListarEstados(self) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

			consulta: str = """SELECT * FROM estados""";
			cursor = conexion.cursor();
			cursor.execute(consulta);

			for elemento in cursor:
				print(elemento);

			cursor.close();
			conexion.close();
		except Exception as ex:
			print(str(ex));

	def ListarEstados2(self) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

			consulta: str = """SELECT * FROM estados""";
			cursor = conexion.cursor();
			cursor.execute(consulta);

			lista: list = [];
			for elemento in cursor:
				entidad: Estados = Estados.Estados();
				entidad.SetId(elemento[0]);
				entidad.SetNombre(elemento[1]);
				lista.append(entidad);

			cursor.close();
			conexion.close();

			for estado in lista:
				print(str(estado.GetId()) + ", " + estado.GetNombre());
		except Exception as ex:
			print(str(ex));

	def ListarInnerJoin(self) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

			consulta: str = """SELECT p.id,
					p.cedula,
					p.nombre,
					p.estado,
					p.fecha,
					p.activo,
					e.id,
					e.nombre
				FROM `personas` p INNER JOIN `estados` e ON p.estado = e.id;""";
			cursor = conexion.cursor();
			cursor.execute(consulta);

			for elemento in cursor:
				print(elemento);

			cursor.close();
			conexion.close();
		except Exception as ex:
			print(str(ex));

	def InsertBasico(self) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

			consulta: str = """INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Test');""";
			cursor = conexion.cursor();
			cursor.execute(consulta);
			cursor.commit();

			cursor.close();
			conexion.close();
		except Exception as ex:
			print(str(ex));

	def ListarProcedimiento(self) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);

			consulta: str = """{CALL proc_select_estados();}""";
			cursor = conexion.cursor();
			cursor.execute(consulta);

			lista: list = [];
			for elemento in cursor:
				entidad: Estados = Estados.Estados();
				entidad.SetId(elemento[0]);
				entidad.SetNombre(elemento[1]);
				lista.append(entidad);

			cursor.close();
			conexion.close();

			for estado in lista:
				print(str(estado.GetId()) + ", " + estado.GetNombre());
		except Exception as ex:
			print(str(ex));

	def InsertBasico(self, nombre: str) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);
			cursor = conexion.cursor();

			consulta: str = "{CALL proc_insert_estados('" + nombre + "', @Respuesta);}";
			cursor.execute(consulta);

			consulta = "SELECT @Respuesta;";
			cursor.execute(consulta);
			print(cursor.fetchone()[0]);
			cursor.commit();

			cursor.close();
			conexion.close();
		except Exception as ex:
			print(str(ex));
   
	def InsertarPersona(self, cedula: str, nombre: str, estado: int, fecha: datetime.datetime, activo: bool) -> None:
		try:
			conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);
			cursor = conexion.cursor();

			consulta: str = "{CALL proc_insert_persona(?, ?, ?, ?, ?);}";
			parametros = (cedula, nombre, estado, fecha.strftime('%Y-%m-%d %H:%M:%S'), activo)


			cursor.execute(consulta, parametros)
			conexion.commit()
	
			cursor.close();
			conexion.close();
		except Exception as ex:
			print(str(ex));