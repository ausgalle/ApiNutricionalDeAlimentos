class AlimentoCategoria:
    id_alimento_categoria: int = 0
    id_alimento: int = 0
    id_categoria: int = 0

    def GetIdAlimentoCategoria(self) -> int:
        return self.id_alimento_categoria

    def SetIdAlimentoCategoria(self, value: int) -> None:
        self.id_alimento_categoria = value

    def GetIdAlimento(self) -> int:
        return self.id_alimento

    def SetIdAlimento(self, value: int) -> None:
        self.id_alimento = value

    def GetIdCategoria(self) -> int:
        return self.id_categoria

    def SetIdCategoria(self, value: int) -> None:
        self.id_categoria = value
