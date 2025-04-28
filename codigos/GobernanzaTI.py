import datetime
from codigos.Prototipo import AuthService

class ITGovernance:
    def __init__(self):
        self.audit_logs = []
        self.risk_register = []
    
    def log_audit(self, action, user, status):
        entry = {
            "timestamp": datetime.now(), 
            "action": action,
            "user": user,
            "status": status
        }
        self.audit_logs.append(entry)
    
    def register_risk(self, risk):
        self.risk_register.append({
            "id": len(self.risk_register) + 1,
            "description": risk,
            "status": "Open"
        })
    
    def generate_report(self, standard):
        if standard == "ISO38500":
            return {
                "strategic_alignment": self._check_alignment(),
                "value_delivery": self._check_value(),
                "risk_management": len(self.risk_register)
            }
        elif standard == "COBIT":
            return {
                "processes_covered": ["APO01", "DSS02"],
                "audit_entries": len(self.audit_logs)
            }

# Integración con servicios existentes
it_governance = ITGovernance()

# Auditoría en el servicio de autenticación
class AuthServiceWithGovernance(AuthService): 
    def login(self, username, password):
        result = super().login(username, password)
        status = "success" if result else "failed"
        it_governance.log_audit("login_attempt", username, status)
        return result