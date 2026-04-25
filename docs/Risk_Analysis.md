# Risk Analysis & Mitigation Strategy
**Project:** Distributed Material Handling System
**Objective:** Identify technical risks and define mitigation logic within the PLC software.

| Risk ID | Technical Risk | Impact | Mitigation Strategy (Software/Logic) |
| :--- | :--- | :--- | :--- |
| **R01** | Communication Loss (Master-Sub) | System Halt / Collision | Implement "Heartbeat" monitoring. If heartbeat fails, Sub-PLC enters "Graceful Stop" or "Local Accumulation" mode. |
| **R02** | Conveyor Jam (PE Blocked) | Motor Overload / Fire | Implement Jam Timer. If PE is blocked > 5s while motor is running, trigger Jam Alarm and stop upstream zones. |
| **R03** | Diverter Feedback Failure | Routing Error | Position feedback monitoring. If "In Position" not reached within 2s, trigger fault and route items to "Reject Lane". |
| **R04** | Master PLC Failure | Total System Shutdown | Redundancy or "Local Mode" capability for Sub-PLCs to continue operating independently for simplified flow. |
| **R05** | Network Congestion (Profinet) | Latency in Routing | Segment network using Scalance switches; prioritize I/O traffic over SCADA polling. |

## Fail-Safe Design Principles
1.  **Normally Closed (NC) Logic:** All safety sensors (E-Stops, Guard interlocks) use NC contacts to ensure a wire break triggers a stop.
2.  **Deterministic Cycles:** Critical control logic is placed in OB1 or high-priority cyclic interrupts (OB35).
