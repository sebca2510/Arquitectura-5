# Ejemplo de implementación balanceada
from codigos.Prototipo import AuthService


class MultiFactorAuth:
    def __init__(self):
        self.strict_mode = False  # Configurable por administrador
    
    def authenticate(self, user, password, token=None):
        if self.strict_mode and not token:
            raise Exception("Se requiere token MFA")
        
        # Lógica de autenticación básica
        return AuthService.login(user, password) 