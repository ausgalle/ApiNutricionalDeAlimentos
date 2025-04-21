class Permiso:
    id_permiso: int = 0
    nombre_permiso: str = None
    descripcion: str = None
    nombre_corto: str = None
    fecha_creacion: str = None
    fecha_actualizacion: str = None

    # Métodos getter y setter
    def GetIdPermiso(self) -> int:
        return self.id_permiso

    def SetIdPermiso(self, value: int) -> None:
        self.id_permiso = value

    def GetNombrePermiso(self) -> str:
        return self.nombre_permiso

    def SetNombrePermiso(self, value: str) -> None:
        self.nombre_permiso = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    def GetNombreCorto(self) -> str:
        return self.nombre_corto

    def SetNombreCorto(self, value: str) -> None:
        self.nombre_corto = value

    def GetFechaCreacion(self) -> str:
        return self.fecha_creacion

    def SetFechaCreacion(self, value: str) -> None:
        self.fecha_creacion = value

    def GetFechaActualizacion(self) -> str:
        return self.fecha_actualizacion

    def SetFechaActualizacion(self, value: str) -> None:
        self.fecha_actualizacion = value