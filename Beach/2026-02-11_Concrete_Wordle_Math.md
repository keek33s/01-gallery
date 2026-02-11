# Concrete: Wordle Math vs. Reality
**Source:** `2026-02-08_0111_Wordle_Probability.md`
**Date:** 2026-02-11
**Context:** Inbox

## Original Content
the probability aspect of a wordle game? i mean the permutations and combinations 5 blank and 26 letters

## The Numbers

You asked for the raw permutations. Here is the math, and why it's a lie.

### 1. The Raw Space (The Lie)
If you have 5 slots and 26 letters (repetition allowed), the total number of combinations is:
$$26^5 = 11,881,376$$
This is the "Monkey on a Typewriter" space. It includes `AAAAA`, `XZYBQ`, and `QQQQQ`.

### 2. The Game Space (The Rules)
Wordle doesn't accept "nonsense". It uses a specific dictionary.
- **Valid Guesses:** ~12,972 words (The "Input Space")
- **Actual Solutions:** ~2,315 words (The "Answer Space")

### 3. The Real Probability (Information Theory)
The "probability aspect" of Wordle isn't about hitting 1 in 11 million. It's about **Entropy Reduction**.
- **Starting Entropy:** $\log_2(2315) \approx 11.17$ bits of uncertainty.
- **Your Job:** Each guess must eliminate roughly half the remaining candidates (1 bit) or more to be "efficient."
- **Best Opener:** `SALET` or `TARSE` (mathematically proven to reduce uncertainty the fastest).

**The Insight:**
You aren't playing a game of luck ($1/11,881,376$). You are playing a game of **Binary Search** disguised as vocabulary. Every grey letter cuts the universe in half.
