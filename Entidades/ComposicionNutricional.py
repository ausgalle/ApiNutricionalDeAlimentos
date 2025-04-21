class ComposicionNutricional:
    id_composicion: int = 0
    id_alimento: int = 0
    id_nutriente: int = 0
    cantidad: float = 0.0
    valor_diario_porcentaje: float = 0.0
    notas: str = None

    def GetIdComposicion(self) -> int:
        return self.id_composicion

    def SetIdComposicion(self, value: int) -> None:
        self.id_composicion = value

    def GetIdAlimento(self) -> int:
        return self.id_alimento

    def SetIdAlimento(self, value: int) -> None:
        self.id_alimento = value

    def GetIdNutriente(self) -> int:
        return self.id_nutriente

    def SetIdNutriente(self, value: int) -> None:
        self.id_nutriente = value

    def GetCantidad(self) -> float:
        return self.cantidad

    def SetCantidad(self, value: float) -> None:
        self.cantidad = value

    def GetValorDiarioPorcentaje(self) -> float:
        return self.valor_diario_porcentaje

    def SetValorDiarioPorcentaje(self, value: float) -> None:
        self.valor_diario_porcentaje = value

    def GetNotas(self) -> str:
        return self.notas

    def SetNotas(self, value: str) -> None:
        self.notas = value
