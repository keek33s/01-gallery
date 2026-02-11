# Clarified: Time-Series Decoder
**Source:** `2026-02-10_1527_Dense_Read_ArXiv.md`
**Date:** 2026-02-11
**Context:** Inbox

## Original Content
another dense read that need to be tackled: https://arxiv.org/pdf/2310.10688

## Artifact
The paper is **"A decoder-only foundation model for time-series forecasting"** (Rajat Sen et al., Google Research?).

**The Core Claim:**
They built a GPT for time-series. Instead of tokens = words, tokens = patches of time-series data. It's a decoder-only transformer trained on a massive corpus of time-series data to do zero-shot forecasting.

**How to Tackle This (The "Scan" Strategy):**
Don't read linearly. This is an architecture paper.
1.  **Figure 1 (The Architecture):** Look for how they tokenize the time series. That's the only "new" thing. The rest is standard Transformer.
2.  **Table 1 (Zero-Shot vs Supervised):** Does it actually beat specialized models like N-BEATS or NHITS? (Spoiler: Usually it "approaches" them but wins on generality).
3.  **The "Why":** Why decoder-only? (Usually for generative/probabilistic forecasting).

**Action:**
Spend 10 minutes scanning Figures 1 & 2. If the tokenization makes sense, you've got 80% of the value.
