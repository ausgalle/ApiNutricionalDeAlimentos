class Rol:
    id_rol: int = 0
    nombre_rol: str = None
    descripcion: str = None
    fecha_creacion: str = None
    fecha_actualizacion: str = None

    # Métodos getter y setter
    def GetIdRol(self) -> int:
        return self.id_rol

    def SetIdRol(self, value: int) -> None:
        self.id_rol = value

    def GetNombreRol(self) -> str:
        return self.nombre_rol

    def SetNombreRol(self, value: str) -> None:
        self.nombre_rol = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    def GetFechaCreacion(self) -> str:
        return self.fecha_creacion

    def SetFechaCreacion(self, value: str) -> None:
        self.fecha_creacion = value

    def GetFechaActualizacion(self) -> str:
        return self.fecha_actualizacion

    def SetFechaActualizacion(self, value: str) -> None:
        self.fecha_actualizacion = value