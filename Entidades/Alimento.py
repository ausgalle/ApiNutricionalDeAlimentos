class Alimento:
    id_alimento: int = 0
    nombre_comun: str = None
    nombre_cientifico: str = None
    descripcion: str = None
    tamano_porcion: float = 0.0
    unidad_porcion: str = "gramo"
    imagen_url: str = None
    notas: str = None
    fecha_creacion: str = None
    fecha_actualizacion: str = None

    # Métodos getter y setter
    def GetIdAlimento(self) -> int:
        return self.id_alimento

    def SetIdAlimento(self, value: int) -> None:
        self.id_alimento = value

    def GetNombreComun(self) -> str:
        return self.nombre_comun

    def SetNombreComun(self, value: str) -> None:
        self.nombre_comun = value

    def GetNombreCientifico(self) -> str:
        return self.nombre_cientifico

    def SetNombreCientifico(self, value: str) -> None:
        self.nombre_cientifico = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    def GetTamanoPorcion(self) -> float:
        return self.tamano_porcion

    def SetTamanoPorcion(self, value: float) -> None:
        self.tamano_porcion = value

    def GetUnidadPorcion(self) -> str:
        return self.unidad_porcion

    def SetUnidadPorcion(self, value: str) -> None:
        self.unidad_porcion = value

    def GetImagenUrl(self) -> str:
        return self.imagen_url

    def SetImagenUrl(self, value: str) -> None:
        self.imagen_url = value

    def GetNotas(self) -> str:
        return self.notas

    def SetNotas(self, value: str) -> None:
        self.notas = value

    def GetFechaCreacion(self) -> str:
        return self.fecha_creacion

    def SetFechaCreacion(self, value: str) -> None:
        self.fecha_creacion = value

    def GetFechaActualizacion(self) -> str:
        return self.fecha_actualizacion

    def SetFechaActualizacion(self, value: str) -> None:
        self.fecha_actualizacion = value
