class FuenteDato:
    id_fuente: int = 0
    nombre_fuente: str = None
    descripcion_fuente: str = None
    url_fuente: str = None
    fecha_creacion: str = None
    fecha_actualizacion: str = None

    def GetIdFuente(self) -> int:
        return self.id_fuente

    def SetIdFuente(self, value: int) -> None:
        self.id_fuente = value

    def GetNombreFuente(self) -> str:
        return self.nombre_fuente

    def SetNombreFuente(self, value: str) -> None:
        self.nombre_fuente = value

    def GetDescripcionFuente(self) -> str:
        return self.descripcion_fuente

    def SetDescripcionFuente(self, value: str) -> None:
        self.descripcion_fuente = value

    def GetUrlFuente(self) -> str:
        return self.url_fuente

    def SetUrlFuente(self, value: str) -> None:
        self.url_fuente = value

    def GetFechaCreacion(self) -> str:
        return self.fecha_creacion

    def SetFechaCreacion(self, value: str) -> None:
        self.fecha_creacion = value

    def GetFechaActualizacion(self) -> str:
        return self.fecha_actualizacion

    def SetFechaActualizacion(self, value: str) -> None:
        self.fecha_actualizacion = value
