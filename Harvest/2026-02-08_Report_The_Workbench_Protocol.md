# Report: The Workbench Protocol (Containment & Taxonomy)
- **Date:** 2026-02-08
- **Context:** Managing "Project Sprawl" (Wordle, One-offs) and refining the Seed/Harvest lifecycle.
- **Tags:** #System_Design #Organization #Workbench

## 1. The Workbench (Lab Isolation)
We have a clutter problem. Experiments like "Wordle Monte Carlo" don't belong in `Ocean` (too noisy) or `Ice` (too permanent).

**The Solution:** `WORLD/System/Workbench/`
-   **Structure:**
    -   `Workbench/Scratchpad/`: Throwaway scripts (deleted after 24h).
    -   `Workbench/Labs/[ProjectName]/`: Persistent experiments (e.g., `Wordle_Sim`, `MiniLM_Test`).
-   **Rule:** Nothing in `Workbench` is indexed by the "Daily Scan" unless explicitly promoted to `Harvest`. It is a "Zero-Gravity Zone."

## 2. Taxonomy Refactor: Sprouts vs. Harvest
We are mixing "Project Files" (The Plan) with "Project Outputs" (The Gold).

**The New Lifecycle:**
1.  **Satchel:** Active Seeds (`Seed_ProjectX.md`).
2.  **Sprouts (New):** *Completed* Seeds. The logistical husk of the project.
    -   *Location:* `WORLD/Ice/Backpack/Sprouts/`
    -   *Purpose:* Audit trail. "What did we do?"
3.  **Harvest:** The *Value* generated. Reports, Essays, Codebases, Art.
    -   *Location:* `WORLD/Ice/Backpack/Harvest/`
    -   *Purpose:* The Library. "What did we learn?"

## 3. Action Plan
1.  **Create:** `WORLD/System/Workbench/`.
2.  **Create:** `WORLD/Ice/Backpack/Sprouts/`.
3.  **Move:** Shift `2026-02-06_Seed_Mirage.md` (and others) to `Sprouts` once closed.
4.  **Clean:** Move the "Wordle" scripts from `Ocean/Waves/Inbox` to `Workbench/Labs/Wordle/`.
