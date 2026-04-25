# Engineering Standards & Naming Conventions
**Scope:** PLC & HMI Development Standard

## 1. Naming Standards (IEC 61131-3)
*   **FBs (Function Blocks):** Prefixed with `FB_` (e.g., `FB_Conveyor`).
*   **FCs (Functions):** Prefixed with `FC_` (e.g., `FC_Scaling`).
*   **DBs (Data Blocks):**
    *   `IDB_` for Instance Data Blocks.
    *   `GDB_` for Global Data Blocks.
*   **Variables:**
    *   `i_` for Inputs.
    *   `q_` for Outputs.
    *   `iq_` for In/Out.
    *   `s_` for Static (internal state).
    *   `t_` for Temporary.

## 2. Code Structure (TIA Portal)
*   **OB1 (Main):** Orchestration and top-level state machine.
*   **OB35 (Cyclic):** High-speed PID or critical interlocks.
*   **OB82/OB86:** Diagnostic interrupts for hardware/network failure.

## 3. Programming Languages
*   **SCL (Structured Control Language):** Preferred for complex data handling, loops, and math.
*   **STL (Statement List):** Used for performance-critical interlocks and low-level bit manipulation (Legacy requirement for S7-300).
*   **LAD (Ladder):** Used for simple motor interlocks to aid maintenance team troubleshooting.

## 4. Process Compliance
*   All code changes must be versioned.
*   Comment every block with "Created By", "Date", and "Revision History".
*   No "Magic Numbers" - use Constants in Global DBs.
