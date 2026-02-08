# Seed: Social Physics & HRI Datasets
- Created: 2026-02-04
- Status: Active
- Context: Compiled for Luna's Social AI research (Social Physics, Signals, HRI).

## 1. Social Navigation & Proxemics (Movement)
*Datasets that track how humans move in spaces, respecting social norms.*

*   **ETH Walking Pedestrians:** The gold standard for trajectory prediction.
    *   *Content:* Overhead video of pedestrians in university/hotel settings.
    *   *Use:* Modeling social forces, collision avoidance.
*   **SocialGym 2.0:**
    *   *Type:* Simulator/Benchmark (ROS-based).
    *   *Focus:* Multi-agent social navigation training.
    *   *Link:* [SocialGym2 GitHub](https://github.com/ut-amrl/SocialGym2)
*   **Stanford Drone Dataset (SDD):**
    *   *Content:* Massive dataset of top-down trajectories (bikes, cars, people).
    *   *Use:* Learning flow and interactions in crowded spaces.

## 2. Gaze, Attention & "The Look"
*Where are they looking? Who is the target of attention?*

*   **SCENE-pathy:**
    *   *Focus:* Visual Selective Attention (VSA) in 3D scenes.
    *   *Link:* [SCENE-pathy GitHub](https://github.com/intelligolabs/scene-pathy)
*   **GazeFollow:**
    *   *Content:* Images with annotations of where people are looking.
    *   *Use:* Inferring joint attention.
*   **HARPER (HRI Pose & Gaze):**
    *   *Focus:* 3D Human Pose from the robot's egocentric perspective.
    *   *Link:* [HARPER GitHub](https://github.com/intelligolabs/HARPER)

## 3. Group Dynamics & "The Party" (F-Formations)
*How people stand together and interact in groups.*

*   **SALSA (Synergistic Social Audio Visual Analysis):**
    *   *Setting:* A cocktail party.
    *   *Signals:* Multimodal (Audio, Video, Badges). Tracks who is talking to whom, groups forming/dissolving.
*   **MatchNMingle:**
    *   *Setting:* Speed dating and mingling.
    *   *Signals:* Wearable sensors + Overhead cameras.
    *   *Focus:* Social affinity, group detection.
*   **Cocktail Party Dataset:**
    *   *Focus:* Audio source separation and localization in social settings.

## 4. Grounded Interaction (Language + Action)
*Connecting words to physical reality.*

*   **HuRIC 2.1 (Human Robot Interaction Corpus):**
    *   *Focus:* Natural language commands paired with "Semantic Maps" (spatial understanding).
    *   *Example:* "Take the mug next to the keyboard."
    *   *Link:* [HuRIC GitHub](https://github.com/crux82/huric)
*   **ManiSkill:**
    *   *Focus:* Generalizable manipulation skills.
    *   *Link:* [ManiSkill GitHub](https://github.com/haosulab/ManiSkill)

## 5. Social Signals (Affect/Emotion)
*   **CMU-MOSEI:** The largest dataset for multimodal sentiment and emotion recognition (Video + Audio + Text).
*   **SEMAINE:** Sensitive Artificial Listener (The "Avatar" interviews). Great for nodding, backchanneling, and emotional alignment.

## Action Items
- [ ] Locate download links for **SALSA** (often hidden behind request forms).
- [ ] Clone **HuRIC** for schema analysis.
- [ ] Check **HuggingFace Datasets** for "Social interactions".
