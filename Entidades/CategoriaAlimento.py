class CategoriaAlimento:
    id_categoria: int = 0
    nombre_categoria: str = None
    descripcion: str = None

    def GetIdCategoria(self) -> int:
        return self.id_categoria

    def SetIdCategoria(self, value: int) -> None:
        self.id_categoria = value

    def GetNombreCategoria(self) -> str:
        return self.nombre_categoria

    def SetNombreCategoria(self, value: str) -> None:
        self.nombre_categoria = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value
