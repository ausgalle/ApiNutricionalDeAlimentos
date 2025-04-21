class RolPermiso:
    id_rol_permiso: int = 0
    id_rol: int = 0
    id_permiso: int = 0

    # Métodos getter y setter
    def GetIdRolPermiso(self) -> int:
        return self.id_rol_permiso

    def SetIdRolPermiso(self, value: int) -> None:
        self.id_rol_permiso = value

    def GetIdRol(self) -> int:
        return self.id_rol

    def SetIdRol(self, value: int) -> None:
        self.id_rol = value

    def GetIdPermiso(self) -> int:
        return self.id_permiso

    def SetIdPermiso(self, value: int) -> None:
        self.id_permiso = value