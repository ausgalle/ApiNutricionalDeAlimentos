class EtiquetaNutricional:
    id_etiqueta: int = 0
    nombre_etiqueta: str = None
    descripcion: str = None

    # Métodos getter y setter
    def GetIdEtiqueta(self) -> int:
        return self.id_etiqueta

    def SetIdEtiqueta(self, value: int) -> None:
        self.id_etiqueta = value

    def GetNombreEtiqueta(self) -> str:
        return self.nombre_etiqueta

    def SetNombreEtiqueta(self, value: str) -> None:
        self.nombre_etiqueta = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value