class UnidadMedida:
    id_unidad: int = 0
    nombre_unidad: str = None
    simbolo: str = None
    descripcion: str = None

    def GetIdUnidad(self) -> int:
        return self.id_unidad

    def SetIdUnidad(self, value: int) -> None:
        self.id_unidad = value

    def GetNombreUnidad(self) -> str:
        return self.nombre_unidad

    def SetNombreUnidad(self, value: str) -> None:
        self.nombre_unidad = value

    def GetSimbolo(self) -> str:
        return self.simbolo

    def SetSimbolo(self, value: str) -> None:
        self.simbolo = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value
