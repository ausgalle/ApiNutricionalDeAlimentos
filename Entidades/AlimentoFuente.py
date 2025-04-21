class AlimentoFuente:
    id_alimento_fuente: int = 0
    id_alimento: int = 0
    id_fuente: int = 0
    fecha_actualizacion: str = None
    notas: str = None

    def GetIdAlimentoFuente(self) -> int:
        return self.id_alimento_fuente

    def SetIdAlimentoFuente(self, value: int) -> None:
        self.id_alimento_fuente = value

    def GetIdAlimento(self) -> int:
        return self.id_alimento

    def SetIdAlimento(self, value: int) -> None:
        self.id_alimento = value

    def GetIdFuente(self) -> int:
        return self.id_fuente

    def SetIdFuente(self, value: int) -> None:
        self.id_fuente = value

    def GetFechaActualizacion(self) -> str:
        return self.fecha_actualizacion

    def SetFechaActualizacion(self, value: str) -> None:
        self.fecha_actualizacion = value

    def GetNotas(self) -> str:
        return self.notas

    def SetNotas(self, value: str) -> None:
        self.notas = value
