# System Architecture: Distributed Material Handling
**Project:** Distributed Material Handling System (Multi-PLC)
**Role:** Controls Lead / System Architect

## 1. Network Overview
The system utilizes a multi-tier communication architecture to ensure high availability and deterministic control.

*   **Tier 1: Plant Network (Profinet/Ethernet)**
    *   S7-1500 (Master PLC) communicating with SCADA (WinCC/Ignition).
*   **Tier 2: Field Network (Profinet)**
    *   S7-1500 Master communicating with S7-300 Sub-PLCs (Line Controllers).
    *   PLC-to-PLC communication via I-Device or GET/PUT (standardized blocks).
*   **Tier 3: Device Bus (ASi / Profinet I/O)**
    *   AS-Interface for simple sensors (PEs) and actuators.
    *   Profinet for VFDs (G120) and remote I/O (ET200SP).

## 2. PLC Responsibilities
### Master PLC (S7-1500)
*   **Global Routing:** Manages the routing table and destination tracking.
*   **Load Balancing:** Monitors throughput and diverts items to less congested lines.
*   **SCADA Interface:** Centralized alarm management and HMI status aggregation.

### Sub-PLC / Line Controller (S7-300)
*   **Execution:** High-speed conveyor control, motor interlocks, and local zone accumulation.
*   **Local Diagnostics:** Monitoring motor currents, jam detection, and local E-Stop zones.

## 3. Library Strategy
A TIA Portal Global Library was developed to ensure code consistency across all PLCs.
*   **Standard FBs:** All conveyor zones, motors, and diverters use the same library blocks to reduce commissioning time and simplify maintenance.
