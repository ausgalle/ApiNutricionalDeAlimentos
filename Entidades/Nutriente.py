class Nutriente:
    id_nutriente: int = 0
    nombre_nutriente: str = None
    unidad_medida: str = None

    def GetIdNutriente(self) -> int:
        return self.id_nutriente

    def SetIdNutriente(self, value: int) -> None:
        self.id_nutriente = value

    def GetNombreNutriente(self) -> str:
        return self.nombre_nutriente

    def SetNombreNutriente(self, value: str) -> None:
        self.nombre_nutriente = value

    def GetUnidadMedida(self) -> str:
        return self.unidad_medida

    def SetUnidadMedida(self, value: str) -> None:
        self.unidad_medida = value
