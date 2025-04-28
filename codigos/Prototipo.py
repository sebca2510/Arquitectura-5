
class LoginComponent:
    def render(self):
        return """
        <div class="login-form">
            <input type="text" id="username" placeholder="Usuario">
            <input type="password" id="password" placeholder="Contraseña">
            <button onclick="authService.login()">Ingresar</button>
        </div>
        """

class ScheduleComponent:
    def render(self, schedule_data):
        return f"""
        <div class="schedule">
            <h2>Horario Académico</h2>
            <table>
                {"".join(f"<tr><td>{item['time']}</td><td>{item['course']}</td></tr>" for item in schedule_data)}
            </table>
        </div>
        """


class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.jwt_secret = "uniminuto_secret_2025"

    def login(self, username, password):
        user = self.user_repository.find_by_username(username)
        if user and user["password"] == self._hash_password(password):
            return self._generate_jwt(user)
        return None

    def _generate_jwt(self, user):
        # Simulación JWT
        return f"jwt.{user['role']}.{user['id']}"

class ScheduleService:
    def __init__(self, schedule_repository):
        self.repository = schedule_repository

    def get_student_schedule(self, student_id):
        return self.repository.find_by_student(student_id)


class UserRepository:
    def __init__(self, db_connection):
        self.db = db_connection

    def find_by_username(self, username):
        # Simulación de consulta a DB
        users = {
            "estudiante1": {"id": 1, "username": "estudiante1", "password": "hash123", "role": "student"},
            "profesor1": {"id": 2, "username": "profesor1", "password": "hash456", "role": "teacher"}
        }
        return users.get(username)

class ScheduleRepository:
    def find_by_student(self, student_id):
        # Simulación de datos de horario
        return [
            {"time": "08:00-10:00", "course": "Arquitectura de Software"},
            {"time": "10:00-12:00", "course": "Bases de Datos"}
        ]

if __name__ == "__main__":
    # Inicialización
    db_conn = "postgresql://user:pass@localhost:5432/sga_db"
    user_repo = UserRepository(db_conn)
    auth_service = AuthService(user_repo)
    
    # Simulación de flujo
    print("=== Prototipo SGA ===")
    
    # 1. Autenticación
    jwt_token = auth_service.login("estudiante1", "hash123")
    print(f"\nToken JWT generado: {jwt_token}")
    
    # 2. Obtención de horario
    schedule_repo = ScheduleRepository(db_conn)
    schedule_service = ScheduleService(schedule_repo)
    schedule_data = schedule_service.get_student_schedule(1)
    
    # 3. Renderizado
    schedule_component = ScheduleComponent()
    print("\nInterfaz de horario:")
    print(schedule_component.render(schedule_data))