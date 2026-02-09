# Researched: Social AI Grounding Libraries

**Source:** `2026-02-03_1656_Social_AI_Grounding.md`  
**Date:** 2026-02-09

---

You asked if this exists. It does — in fragments. Here's what's already out there and where the gaps are:

## Existing Work

### 1. Non-Verbal Cue Integration
**Active Projects:**
- **OpenFace** (CMU) – Real-time facial behavior analysis (gaze, head pose, action units). Open-source C++ library.
  - Link: https://github.com/TadasBaltrusaitis/OpenFace
- **Social Signals Interpretation (SSI)** – Framework for multimodal behavior analysis (voice prosody, gesture, micro-expressions).
  - Link: https://github.com/hcmlab/ssi
- **HUMAINE Emotion Annotation** – Standardized schema for annotating social signals in HRI contexts.

**What's Missing:** Real-time libraries that *generate* appropriate non-verbal responses (not just detect). Most work is detection-only.

### 2. Collaborative Task Sequencing
**Active Projects:**
- **ROSPlan** (Robot Operating System extension) – Task planning with human-in-the-loop adaptation.
  - Link: https://github.com/KCL-Planning/ROSPlan
- **Theory of Mind for AI (ATOMIC)** – Commonsense reasoning about social physics (If-Then social rules).
  - Paper: COMET-ATOMIC 2020 (https://arxiv.org/abs/2010.05953)
  - Dataset: https://allenai.org/data/atomic-2020

**What's Missing:** Libraries specifically for turn-taking, interruption-handling, and collaborative flow in real-time dialogue (not just task graphs).

### 3. "Resembling People" (Social Grounding Data)
**Datasets:**
- **MELD** (Multimodal EmotionLines Dataset) – Emotion + context in multi-party conversations.
- **RECOLA** (Remote Collaborative and Affective Interactions) – Video/audio of real collaborative tasks with continuous affective annotations.
- **ParlAI ConvAI2** – Persona-based dialogue, but text-only (no embodiment).

**What's Missing:** Datasets that capture *hesitation*, *repair*, *gaze coordination*, and *joint attention* in naturalistic HRI tasks.

---

## The Gap You're Describing

You're talking about the **integration layer** — a unified library that:
1. **Detects** multi-modal social cues (existing tools do this).
2. **Interprets** them in context (some progress via Theory of Mind models).
3. **Generates** appropriate responses (timing, tone, gesture) in real-time (this barely exists).

Current state: Researchers build custom pipelines for each robot/agent. No standardized "social physics engine."

---

## What This Could Be

**Option A: A Dataset/Benchmark**
- **Name:** "HRI Social Grounding Corpus" or similar.
- **Content:** Annotated multi-modal logs of human-robot collaboration (gaze, gesture, speech timing, task state).
- **Value:** Researchers can train models without building their own data collection rig.
- **Precedent:** See how **ImageNet** standardized vision. This would be the HRI equivalent.

**Option B: A Library/Framework**
- **Name:** "SocialPhysics" or "HRI-Core" (Python + ROS bindings).
- **Modules:**
  - `nonverbal` – Detect/generate gaze, gesture, posture.
  - `turn_taking` – Handle interruptions, backchanneling, silence.
  - `joint_attention` – Track shared focus (object, screen, person).
  - `task_sequencing` – Adaptive planning with human-in-the-loop.
- **Value:** Plug-and-play social behavior for embodied agents.
- **Precedent:** Like **Hugging Face Transformers** but for HRI.

**Option C: A Design Pattern Library**
- **Format:** Documentation + Reference Implementations.
- **Content:** "How to implement collaborative error recovery," "When to use gaze aversion," etc.
- **Value:** Bridges research and product teams. HCI designers can spec social behaviors without reading 50 papers.

---

## Next Steps (If You Want to Pursue This)

1. **Narrow the Scope:** Pick one module (e.g., "Non-Verbal Response Generation").
2. **Audit Existing Tools:** Download OpenFace, SSI, ROSPlan. See what's reusable.
3. **Identify One Missing Piece:** What can't you do with existing tools? Build that.
4. **Prototype on a Real Use Case:** Pick a specific HRI scenario (e.g., "Robot tutoring a child"). Implement the missing library for that context. Generalize later.

---

## Why This Matters

Most "social AI" is chatbots with personality prompts. You're talking about **embodied interaction** — where timing, gaze, and gesture *are* the language. That's under-resourced compared to LLMs.

If you built even a small piece of this (a good dataset, a clean library), it would get used. The HRI community is small but desperate for infrastructure.
