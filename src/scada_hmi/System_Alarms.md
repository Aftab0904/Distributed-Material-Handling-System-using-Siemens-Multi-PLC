# System Alarm Matrix
**Project:** Distributed Material Handling System
**HMI Software:** WinCC Professional / Unified

| Alarm ID | Tag Name | Trigger | Priority | Message Text | Action Required |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A101** | Global_EStop | I0.0 = 0 | Critical (1) | "EMERGENCY STOP ACTIVATED" | Clear physical hazard, pull reset PB. |
| **A201** | Motor_Fault_1 | FB_Motor.Fault | High (2) | "LINE 1 MOTOR OVERLOAD / FEEDBACK FAIL" | Check motor breaker and VFD status. |
| **A301** | Jam_Detected_1 | FB_Zone.Jam | Medium (3) | "CONVEYOR 1 JAM DETECTED" | Remove blockage from Photo-eye 1. |
| **A401** | Comm_Fail_300 | Profinet.Error | High (2) | "COMMUNICATION LOST: LINE CONTROLLER 1" | Check ethernet cable and switch status. |
| **A501** | Diverter_Err | FB_Diverter.Err | Medium (3) | "DIVERTER 1 FEEDBACK TIMEOUT" | Verify pneumatic pressure and limit switches. |

## Alarm Grouping
*   **Group 1 (Safety):** Immediate stop of all power.
*   **Group 2 (Process):** Interlocked stop of upstream zones.
*   **Group 3 (Maintenance):** Information only, no automatic stop.
