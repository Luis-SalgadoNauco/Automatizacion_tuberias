from typing import Dict
from datetime import datetime, timedelta
import logging

# ----------------------------
# Configuración de logging
# ----------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("incident_response")

# ----------------------------
# Post-mortem
# ----------------------------
def create_post_mortem_template(incident_data: Dict) -> str:
    return f"""
# Post-Mortem: {incident_data['title']}

## Executive Summary
{incident_data.get('summary', 'N/A')}

## Timeline
- Detection: {incident_data.get('detection_time')}
- Start: {incident_data.get('start_time')}
- End: {incident_data.get('end_time')}
- Duration: {incident_data.get('duration')}

## Impact
- Users affected: {incident_data.get('users_affected')}
- Business impact: {incident_data.get('business_impact')}

## Root Cause
{incident_data.get('root_cause')}

## Resolution Steps
{chr(10).join(f"- {step}" for step in incident_data.get('resolution_steps', []))}

## What went well
{chr(10).join(f"- {item}" for item in incident_data.get('went_well', []))}

## Improvements
{chr(10).join(f"- {item}" for item in incident_data.get('improvements', []))}

## Action Items
{chr(10).join(f"- [ ] {item}" for item in incident_data.get('action_items', []))}

## Prevention
{chr(10).join(f"- {item}" for item in incident_data.get('prevention', []))}

---
Generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""


# ----------------------------
# Incident Runbook
# ----------------------------
class IncidentRunbook:
    """Runbook automatizado para respuesta a incidentes"""

    def __init__(self):
        self.incident_types = self._define_incident_types()
        self.escalation_matrix = self._define_escalation()

    def _define_incident_types(self) -> Dict:
        return {
            "pipeline_down": {
                "severity": "CRITICAL",
                "auto_response": True,
                "timeout": timedelta(minutes=15),
                "steps": [
                    "check_airflow_scheduler",
                    "check_database_connectivity",
                    "restart_failed_services",
                    "verify_pipeline_recovery",
                ],
            }
        }

    def _define_escalation(self) -> Dict:
        return {
            "CRITICAL": {
                "5min": "alert_lead_engineer",
                "15min": "alert_engineering_manager",
                "30min": "alert_vp_engineering",
            }
        }

    def handle_incident(self, incident_type: str, context: Dict) -> Dict:
        if incident_type not in self.incident_types:
            raise ValueError("Unknown incident type")

        config = self.incident_types[incident_type]
        start_time = datetime.now()

        logger.info(
            f"Handling {incident_type} (severity: {config['severity']})"
        )

        results = {
            "incident_type": incident_type,
            "severity": config["severity"],
            "start_time": start_time.isoformat(),
            "steps_executed": [],
            "auto_recovery_attempted": config["auto_response"],
        }

        for step in config["steps"]:
            result = self._execute_step(step)
            results["steps_executed"].append(result)
            if not result["success"]:
                break

        results["resolved"] = self._verify_resolution()
        results["end_time"] = datetime.now().isoformat()
        results["duration_seconds"] = (
            datetime.now() - start_time
        ).total_seconds()

        if not results["resolved"]:
            self._escalate_incident(
                config["severity"], results["duration_seconds"]
            )

        return results

    # ----------------------------
    # Steps
    # ----------------------------
    def _execute_step(self, step_name: str) -> Dict:
        step_map = {
            "check_airflow_scheduler": lambda: self._check_service(
                "airflow-scheduler"
            ),
            "check_database_connectivity": self._check_database_connection,
            "restart_failed_services": lambda: self._restart_services(
                ["airflow-scheduler", "airflow-webserver"]
            ),
            "verify_pipeline_recovery": self._verify_pipeline_status,
        }

        try:
            result = step_map[step_name]()
            logger.info(f"Step {step_name} completed")
            return {"step": step_name, "success": True, "result": result}
        except Exception as e:
            return {"step": step_name, "success": False, "error": str(e)}

    # ----------------------------
    # Escalation
    # ----------------------------
    def _escalate_incident(self, severity: str, duration_seconds: float):
        for time_threshold, action in self.escalation_matrix.get(
            severity, {}
        ).items():
            if duration_seconds >= self._parse_time(time_threshold):
                logger.warning(f"Escalating incident: {action}")

    # ----------------------------
    # Simulated actions
    # ----------------------------
    def _check_service(self, service_name: str):
        return {"service": service_name, "status": "running"}

    def _check_database_connection(self):
        return {"connected": True, "latency_ms": 20}

    def _restart_services(self, services):
        return {"restarted": services}

    def _verify_pipeline_status(self):
        return {"pipelines_failed": 0}

    def _verify_resolution(self):
        return True

    def _parse_time(self, time_str: str) -> int:
        if "min" in time_str:
            return int(time_str.replace("min", "")) * 60
        if "h" in time_str:
            return int(time_str.replace("h", "")) * 3600
        return 0


# ----------------------------
# Simulación
# ----------------------------
if __name__ == "__main__":
    runbook = IncidentRunbook()

    response = runbook.handle_incident(
        "pipeline_down",
        {"triggered_by": "alert_pipeline_down"},
    )

    print("\nRespuesta a incidente:")
    print(f"Tipo: {response['incident_type']}")
    print(f"Severidad: {response['severity']}")
    print(f"Resuelto: {response['resolved']}")
    print(f"Duración: {response['duration_seconds']:.1f}s")
    print("Pasos ejecutados:")
    for step in response["steps_executed"]:
        print(f"  {'✅' if step['success'] else '❌'} {step['step']}")

    incident_data = {
        "title": "Pipeline Down – Airflow Scheduler",
        "summary": "El scheduler de Airflow dejó de responder.",
        "detection_time": "2026-01-24 10:05",
        "start_time": "2026-01-24 10:00",
        "end_time": "2026-01-24 10:15",
        "duration": "15 minutos",
        "users_affected": 3,
        "business_impact": "Retraso en carga diaria",
        "root_cause": "Consumo excesivo de memoria",
        "resolution_steps": [
            "Revisión del scheduler",
            "Reinicio del servicio",
            "Validación de DAGs",
        ],
        "went_well": ["Alerta automática", "Recuperación rápida"],
        "improvements": ["Monitoreo de memoria"],
        "action_items": [
            "Agregar alerta de memoria",
            "Documentar procedimiento",
        ],
        "prevention": ["Auto-restart", "Escalado preventivo"],
    }

    post_mortem = create_post_mortem_template(incident_data)
    print(post_mortem)

with open("post_mortem_pipeline_down.md", "w") as f:
    f.write(post_mortem)

print("\n📄 Post-mortem guardado como post_mortem_pipeline_down.md")
