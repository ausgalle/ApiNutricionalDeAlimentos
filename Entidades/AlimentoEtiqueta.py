class AlimentoEtiqueta:
    id_alimento_etiqueta: int = 0
    id_alimento: int = 0
    id_etiqueta: int = 0

    # Métodos getter y setter
    def GetIdAlimentoEtiqueta(self) -> int:
        return self.id_alimento_etiqueta

    def SetIdAlimentoEtiqueta(self, value: int) -> None:
        self.id_alimento_etiqueta = value

    def GetIdAlimento(self) -> int:
        return self.id_alimento

    def SetIdAlimento(self, value: int) -> None:
        self.id_alimento = value

    def GetIdEtiqueta(self) -> int:
        return self.id_etiqueta

    def SetIdEtiqueta(self, value: int) -> None:
        self.id_etiqueta = value