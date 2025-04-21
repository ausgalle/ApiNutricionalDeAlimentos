class Usuario:
    id_usuario: int = 0
    nombre_usuario: str = None
    contrasena: str = None
    email: str = None
    id_rol: int = None
    fecha_registro: str = None
    ultimo_login: str = None
    activo: bool = True

    # Métodos getter y setter
    def GetIdUsuario(self) -> int:
        return self.id_usuario

    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    def GetNombreUsuario(self) -> str:
        return self.nombre_usuario

    def SetNombreUsuario(self, value: str) -> None:
        self.nombre_usuario = value

    def GetContrasena(self) -> str:
        return self.contrasena

    def SetContrasena(self, value: str) -> None:
        self.contrasena = value

    def GetEmail(self) -> str:
        return self.email

    def SetEmail(self, value: str) -> None:
        self.email = value

    def GetIdRol(self) -> int:
        return self.id_rol

    def SetIdRol(self, value: int) -> None:
        self.id_rol = value

    def GetFechaRegistro(self) -> str:
        return self.fecha_registro

    def SetFechaRegistro(self, value: str) -> None:
        self.fecha_registro = value

    def GetUltimoLogin(self) -> str:
        return self.ultimo_login

    def SetUltimoLogin(self, value: str) -> None:
        self.ultimo_login = value

    def GetActivo(self) -> bool:
        return self.activo

    def SetActivo(self, value: bool) -> None:
        self.activo = value