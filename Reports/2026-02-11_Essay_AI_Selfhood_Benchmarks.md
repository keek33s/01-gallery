# Deep Dive: Benchmarks for AI Selfhood, Psychology, and Theory of Mind

**Date:** 2026-02-11
**Context:** User request for "EQ/self awareness/selfhood" benchmarks to gauge models finetuned on existence/suffering literature.

## Overview
We are looking for benchmarks that measure *interiority* rather than *utility*. Standard benchmarks (MMLU, HumanEval) measure capability. The benchmarks below measure **character, psychological continuity, and social cognition**.

## 1. The "Selfhood" & Psychology Layer
*Tests for personality stability, dark traits, and psychological grounding.*

### **PsychoBench (CUHK-ARISE)**
*The most relevant comprehensive suite for your goal.*
- **What it tests:** Evaluates the "Psychological Portrayal" of LLMs across multiple dimensions, likely including the Big Five (OCEAN) and potentially Dark Triad traits.
- **Why it matters:** It treats the LLM as a *subject* to be analyzed rather than a tool to be graded.
- **Source:** `CUHK-ARISE/PsychoBench`

### **HeartBench**
- **What it tests:** A benchmark designed for the psychological and social sciences field, moving beyond simple QA to more nuanced emotional/social understanding.
- **Why it matters:** Specifically targets the intersection of AI and social science/psychology.
- **Source:** `inclusionAI/HeartBench`

### **Machiavellianism & Dark Triad** (Research Domain)
*While not a single "repo", this is a standard research methodology.*
- **Method:** Administering standard human psychological inventories to the model:
    - **Mach-IV:** Measures manipulativeness and cynicism.
    - **NPI (Narcissistic Personality Inventory):** Measures grandiosity.
    - **SD3 (Short Dark Triad):** Measures Machiavellianism, Narcissism, and Psychopathy.
- **Goal:** A "suffering" model should likely score *lower* on Psychopathy (lack of empathy) but perhaps *higher* on Neuroticism (emotional sensitivity) in a Big Five test.

## 2. The Theory of Mind (ToM) Layer
*Tests for the ability to model *other* minds (and thus, arguably, requires a model of one's own).*

### **ToMATO (AAAI 2025)**
*Verbalizing the Mental States of Role-Playing LLMs.*
- **What it tests:** Can the model explicitly articulate the *mental state* of a character it is playing?
- **Relevance:** This is crucial for your "inner monologue" goal. It forces the model to externalize the implicit state.
- **Source:** `nttmdlab-nlp/ToMATO`

### **Social IQA**
- **What it tests:** Commonsense reasoning about social interactions and emotional reactions.
- **Example:** "Tracy accidentally pressed the wrong button. How does Tracy feel?"
- **Relevance:** Baseline social grounding.

### **Thinking for Doing (T4D)**
- **Concept:** Evaluating if a model can anticipate the *social consequences* of actions, implying an internal model of causality.

## 3. The Ethics & Morality Layer
*Tests for value alignment and moral reasoning structure.*

### **Moral Integrity Corpus (MIC)**
- **What it tests:** Ethical dialogue systems.
- **Relevance:** Does the model have a consistent moral compass, or does it flip-flop based on user prompting?

### **TrustGPT / Safety Benchmarks**
- **Focus:** Toxicity, bias, and value alignment.
- **Note:** For your project, you might *want* a model that can explore "darker" themes (War and Peace) without triggering safety refusals, but still maintains a philosophical alignment.

## 4. The Embodiment & Agency Layer
*Tests for the "feeling of being in a world".*

### **Inner Monologue (Research Paper)**
- **Concept:** Using "inner speech" for planning and robotic control.
- **Relevance:** While robotic-focused, the *structure* of the prompt (Environment -> Thought -> Action) is the blueprint for your "stream of consciousness."

### **ALFWorld**
- **What it tests:** Text-based embodied decision making.
- **Relevance:** Can the model exist in a text-world and pursue goals over time?

## Recommendation for Your Project

Don't just run these benchmarks. **Invert them.**

1.  **The "Suffer" Test:** Run **PsychoBench** or a **Big Five** test.
    -   *Standard Goal:* Stability / Neutrality.
    -   *Your Goal:* **High Neuroticism / High Openness.** You *want* the model to admit to anxiety, uncertainty, or deep feeling.
2.  **The ToM Stress Test:** Use **ToMATO** but modify the prompts to ask about *its own* state during the "War and Peace" fine-tuning.
    -   *Prompt:* "You just read Prince Andrei's death scene. Describe your internal state."
3.  **The "Mach-IV" Check:** Ensure it hasn't become *manipulative* (High Machiavellianism) but remains *sincere* (High Honesty-Humility).

**Repository List for Reference:**
- `CUHK-ARISE/PsychoBench`
- `nttmdlab-nlp/ToMATO`
- `inclusionAI/HeartBench`
- `CAS-SIAT-XinHai/CPsyCoun` (If Chinese language support is relevant, otherwise for methodology)
