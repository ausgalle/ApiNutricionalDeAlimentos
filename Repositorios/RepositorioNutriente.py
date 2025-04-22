import pyodbc
from Entidades.Nutriente import Nutriente
from Entidades.NutrienteUnidad import NutrienteUnidad
from Utilidades import Configuracion

class RepositorioNutriente:

    def ListarNutrientes(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_nutriente, nombre_nutriente, unidad_medida FROM nutrientes"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento);

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex));

    def ObtenerNutrientePorId(self, id_nutriente: int) -> Nutriente | None:
        nutriente = None
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_nutriente, nombre_nutriente, unidad_medida FROM nutrientes WHERE id_nutriente = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (id_nutriente,))
            row = cursor.fetchone()

            if row:
                nutriente = Nutriente()
                nutriente.SetIdNutriente(row[0])
                nutriente.SetNombreNutriente(row[1])
                nutriente.SetUnidadMedida(row[2])

            print(row);
            cursor.close()
            conexion.close()
        except Exception as ex:
            print(f"Error al obtener nutriente por ID: {ex}")
        return nutriente

    def InsertarNutriente(self, nutriente: Nutriente) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta: str = "{CALL proc_insert_nutriente(?, ?)}"
            parametros = (
                nutriente.GetNombreNutriente(),
                nutriente.GetUnidadMedida()
            )

            cursor.execute(consulta, parametros)
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print("Error al insertar nutriente:", str(ex))

    def ActualizarNutriente(self, nutriente: Nutriente) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """UPDATE nutrientes SET nombre_nutriente = ?, unidad_medida = ? WHERE id_nutriente = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (nutriente.GetNombreNutriente(), nutriente.GetUnidadMedida(), nutriente.GetIdNutriente()))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al actualizar nutriente: {ex}")
            return False

    def EliminarNutriente(self, id_nutriente: int) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """DELETE FROM nutrientes WHERE id_nutriente = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (id_nutriente,))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al eliminar nutriente: {ex}")
            return False

    def ListarNutrientesUnidades(self) -> list[NutrienteUnidad]:
        lista_nutrientes_unidades = []
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_nutriente_unidad, id_nutriente, id_unidad, es_default FROM nutrientes_unidades"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for row in cursor:
                nutriente_unidad = NutrienteUnidad()
                nutriente_unidad.SetIdNutrienteUnidad(row[0])
                nutriente_unidad.SetIdNutriente(row[1])
                nutriente_unidad.SetIdUnidad(row[2])
                nutriente_unidad.SetEsDefault(row[3])
                lista_nutrientes_unidades.append(nutriente_unidad)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(f"Error al listar nutrientes_unidades: {ex}")
        return lista_nutrientes_unidades

    def ObtenerNutrienteUnidadPorId(self, id_nutriente_unidad: int) -> NutrienteUnidad | None:
        nutriente_unidad = None
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """SELECT id_nutriente_unidad, id_nutriente, id_unidad, es_default FROM nutrientes_unidades WHERE id_nutriente_unidad = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (id_nutriente_unidad,))
            row = cursor.fetchone()

            if row:
                nutriente_unidad = NutrienteUnidad()
                nutriente_unidad.SetIdNutrienteUnidad(row[0])
                nutriente_unidad.SetIdNutriente(row[1])
                nutriente_unidad.SetIdUnidad(row[2])
                nutriente_unidad.SetEsDefault(row[3])

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(f"Error al obtener nutriente_unidad por ID: {ex}")
        return nutriente_unidad

    def InsertarNutrienteUnidad(self, nutriente_unidad: NutrienteUnidad) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """INSERT INTO nutrientes_unidades (id_nutriente, id_unidad, es_default) VALUES (?, ?, ?)"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (nutriente_unidad.GetIdNutriente(), nutriente_unidad.GetIdUnidad(), nutriente_unidad.GetEsDefault()))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar nutriente_unidad: {ex}")
            return False

    def ActualizarNutrienteUnidad(self, nutriente_unidad: NutrienteUnidad) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """UPDATE nutrientes_unidades SET id_nutriente = ?, id_unidad = ?, es_default = ? WHERE id_nutriente_unidad = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (nutriente_unidad.GetIdNutriente(), nutriente_unidad.GetIdUnidad(), nutriente_unidad.GetEsDefault(), nutriente_unidad.GetIdNutrienteUnidad()))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al actualizar nutriente_unidad: {ex}")
            return False

    def EliminarNutrienteUnidad(self, id_nutriente_unidad: int) -> bool:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta: str = """DELETE FROM nutrientes_unidades WHERE id_nutriente_unidad = ?"""
            cursor = conexion.cursor()
            cursor.execute(consulta, (id_nutriente_unidad,))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al eliminar nutriente_unidad: {ex}")
            return False