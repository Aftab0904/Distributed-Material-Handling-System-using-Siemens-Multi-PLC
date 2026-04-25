# Commissioning & Site Handover Checklist
**Phase:** Execution / Handover

## 1. Hardware & Connectivity
- [ ] Verify 24V DC supply at all remote I/O (ET200SP) and ASi gateways.
- [ ] Profinet Network Topology scan (PRONETA) matches electrical drawings.
- [ ] ASi bus addressing completed for all PE sensors and Solenoids.
- [ ] E-Stop circuit continuity test and safety relay function check.

## 2. PLC Software & Communication
- [ ] Master S7-1500 can Ping all Sub S7-300 PLCs.
- [ ] I-Device communication mapping verified (Status bits, Control bits).
- [ ] Heartbeat logic tested by disconnecting Profinet cable (Confirm "R01" mitigation).
- [ ] Watchdog timers set correctly for all VFDs.

## 3. Functional Testing (Conveyance)
- [ ] Motor rotation check for all lines (Clockwise/Counter-clockwise).
- [ ] Zone accumulation logic: Verify Zone A stops when Zone B is full.
- [ ] Diverter switching: Verify timing between PE trigger and Solenoid activation.
- [ ] Full Load Test: Run system at 100% capacity for 4 hours without jams.

## 4. SCADA/HMI
- [ ] All alarms appearing on WinCC alarm screen with correct priority.
- [ ] Real-time throughput (items/min) dashboard verified against manual count.
- [ ] Maintenance override buttons (Manual/Auto) function correctly.
