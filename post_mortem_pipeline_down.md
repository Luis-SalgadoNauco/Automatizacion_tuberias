
# Post-Mortem: Pipeline Down – Airflow Scheduler

## Executive Summary
El scheduler de Airflow dejó de responder.

## Timeline
- Detection: 2026-01-24 10:05
- Start: 2026-01-24 10:00
- End: 2026-01-24 10:15
- Duration: 15 minutos

## Impact
- Users affected: 3
- Business impact: Retraso en carga diaria

## Root Cause
Consumo excesivo de memoria

## Resolution Steps
- Revisión del scheduler
- Reinicio del servicio
- Validación de DAGs

## What went well
- Alerta automática
- Recuperación rápida

## Improvements
- Monitoreo de memoria

## Action Items
- [ ] Agregar alerta de memoria
- [ ] Documentar procedimiento

## Prevention
- Auto-restart
- Escalado preventivo

---
Generated at 2026-01-24 19:13:45
