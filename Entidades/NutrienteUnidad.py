class NutrienteUnidad:
    id_nutriente_unidad: int = 0
    id_nutriente: int = 0
    id_unidad: int = 0
    es_default: bool = False

    # Métodos getter y setter
    def GetIdNutrienteUnidad(self) -> int:
        return self.id_nutriente_unidad

    def SetIdNutrienteUnidad(self, value: int) -> None:
        self.id_nutriente_unidad = value

    def GetIdNutriente(self) -> int:
        return self.id_nutriente

    def SetIdNutriente(self, value: int) -> None:
        self.id_nutriente = value

    def GetIdUnidad(self) -> int:
        return self.id_unidad

    def SetIdUnidad(self, value: int) -> None:
        self.id_unidad = value

    def GetEsDefault(self) -> bool:
        return self.es_default

    def SetEsDefault(self, value: bool) -> None:
        self.es_default = value